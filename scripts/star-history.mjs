#!/usr/bin/env node
/**
 * Generate a star-history SVG from the GitHub API.
 *
 * star-history.com's public API started returning 404/500, which left a broken
 * image in the README. This renders the same chart from data we already own.
 *
 * Reconstructing the curve does not need all N stargazers: asking for
 * `per_page=1&page=N` returns exactly the Nth one, so a few dozen sampled
 * points describe the shape as well as tens of thousands would. That keeps this
 * to ~40 API calls instead of ~350.
 *
 *   GITHUB_TOKEN=... node scripts/star-history.mjs owner/repo images/star-history.svg
 *   node scripts/star-history.mjs --self-check
 */

import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname } from 'node:path';
import { pathToFileURL } from 'node:url';

const API = 'https://api.github.com';
const SAMPLES = 40;
const W = 800, H = 400;
const PAD_L = 70, PAD_R = 30, PAD_T = 30, PAD_B = 50;

async function get(url, token, accept = 'application/vnd.github+json') {
  const headers = { Accept: accept, 'User-Agent': 'star-history-generator' };
  if (token) headers.Authorization = `Bearer ${token}`;
  const res = await fetch(url, { headers });
  if (!res.ok) {
    const err = new Error(`HTTP ${res.status} for ${url}`);
    err.status = res.status;
    throw err;
  }
  return res.json();
}

// Only the stargazers endpoint documents/needs this media type - it's what
// makes starred_at appear in the response. Sending it on other endpoints
// (like /repos/{repo}) is undocumented behaviour we shouldn't rely on.
const STAR_JSON = 'application/vnd.github.star+json';

export async function fetchPoints(repo, token, samples = SAMPLES) {
  const meta = await get(`${API}/repos/${repo}`, token);
  const total = meta.stargazers_count;
  if (!total) return [];

  // Evenly spaced 1-based indices, always including the first and last star.
  let indices;
  if (total <= samples) {
    indices = Array.from({ length: total }, (_, i) => i + 1);
  } else {
    const step = (total - 1) / (samples - 1);
    indices = [...new Set(
