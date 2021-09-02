import { useEffect, useMemo, useState } from "react";
import {
  ArrowRight,
  BookOpen,
  Boxes,
  CheckCircle2,
  Code2,
  Copy,
  ExternalLink,
  FileText,
  Filter,
  GitBranch,
  Github,
  GraduationCap,
  Layers3,
  Network,
  Play,
  Search,
  Terminal,
  Workflow,
  Zap,
} from "lucide-react";
import { catalog, slugify, stripMarkdown } from "./content.js";

const routeLabels = [
  { path: "/", label: "Atlas" },
  { path: "/course", label: "Course" },
  { path: "/agents", label: "Agents" },
  { path: "/use-cases", label: "Use cases" },
  { path: "/frameworks", label: "Frameworks" },
];

function useHashRoute() {
  const [route, setRoute] = useState(() => window.location.hash.slice(1) || "/");

  useEffect(() => {
    const onHashChange = () => setRoute(window.location.hash.slice(1) || "/");
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, []);

  return route;
}

function pathFor(route) {
  return `#${route}`;
}

function normalize(value = "") {
  return value.toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
}

function matchesQuery(item, query) {
  if (!query) return true;
  const haystack = normalize(
    [
      item.title,
      item.description,
      item.framework,
      item.industry,
      item.sourceHeading,
      item.tags?.join(" "),
    ].join(" "),
  );
  return normalize(query)
    .split(" ")
    .filter(Boolean)
    .every((part) => haystack.includes(part));
}

function getIntro(markdown = "", fallback = "") {
  const lines = markdown
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .filter((line) => !line.startsWith("#") && !line.startsWith("```"));

  return stripMarkdown(lines.find((line) => line.length > 30) || fallback).slice(0, 260);
}

function Shell({ route, children }) {
  return (
    <div className="app-shell">
      <header className="topbar">
        <a className="brand" href={pathFor("/")}>
          <span className="brand-mark">
            <Network size={18} aria-hidden="true" />
          </span>
          <span>
            <strong>AI Agents Atlas</strong>
            <small>500+ project map</small>
          </span>
        </a>

        <nav className="nav-links" aria-label="Main navigation">
          {routeLabels.map((item) => (
            <a
              className={
                route === item.path || (item.path !== "/" && route.startsWith(`${item.path}/`))
                  ? "active"
                  : ""
              }
              href={pathFor(item.path)}
              key={item.path}
            >
              {item.label}
            </a>
          ))}
        </nav>

        <a className="icon-link" href="https://github.com/ashishpatel26/500-AI-Agents-Projects">
          <Github size={18} aria-hidden="true" />
          <span>GitHub</span>
        </a>
      </header>
      <main>{children}</main>
    </div>
  );
}

function StatStrip() {
  const stats = [
    { label: "Runnable agents", value: catalog.agents.length, icon: Code2 },
    { label: "README use cases", value: catalog.useCases.length, icon: Boxes },
    { label: "Framework families", value: catalog.frameworks.length, icon: Workflow },
    { label: "Course lessons", value: catalog.courseLessons.length, icon: GraduationCap },
  ];

  return (
    <section className="stat-strip" aria-label="Repository statistics">
      {stats.map((stat) => {
        const Icon = stat.icon;
