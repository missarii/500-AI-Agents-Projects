  const ok = (c, m) => { if (!c) throw new Error(`self-check failed: ${m}`); };

  ok(svg.startsWith('<svg'), 'must emit an svg root');
  ok(svg.includes('1,000 stars'), 'final count must be rendered');
  ok(svg.includes('polyline'), 'curve must be drawn');

  // Monotonic time must map to monotonic x, and stay inside the plot area.
  const xs = svg.match(/<polyline points="([^"]+)"/)[1]
    .split(' ').map((p) => parseFloat(p.split(',')[0]));
  ok(xs.every((x, i) => i === 0 || x >= xs[i - 1]), 'x must increase with time');
  ok(xs.every((x) => x >= PAD_L - 0.5 && x <= W - PAD_R + 0.5), 'curve must stay in frame');

  const ys = svg.match(/<polyline points="([^"]+)"/)[1]
    .split(' ').map((p) => parseFloat(p.split(',')[1]));
  ok(ys.every((y) => y >= PAD_T - 0.5 && y <= H - PAD_B + 0.5), 'curve must stay vertically in frame');

  const { ticks, top } = niceTicks(35133);
  ok(top >= 35133, 'axis must not clip the highest value');
  ok(ticks[0] === 0 && ticks.every((t, i) => i === 0 || t > ticks[i - 1]), 'ticks ascend from zero');

  ok(fmt(1000) === '1k' && fmt(1500) === '1.5k' && fmt(999) === '999', 'number formatting');
  ok(renderSvg([], 'x/y').startsWith('<svg'), 'zero stars must not crash');

  console.log('self-check OK');
}

async function main() {
  if (process.argv.includes('--self-check')) return selfCheck(), 0;

  const repo = process.argv[2] || process.env.GITHUB_REPOSITORY;
  const out = process.argv[3] || 'images/star-history.svg';
  if (!repo) {
    console.error('usage: star-history.mjs owner/repo [out.svg]');
    return 2;
  }

  console.log(`sampling ${repo} ...`);
  const points = await fetchPoints(repo, process.env.GITHUB_TOKEN);
  if (!points.length) {
    console.error('no stargazer data returned');
    return 1;
  }

  mkdirSync(dirname(out) || '.', { recursive: true });
  writeFileSync(out, renderSvg(points, repo), 'utf8');
  console.log(`wrote ${out} from ${points.length} sampled points, ${points[points.length - 1][1]} stars`);
  return 0;
}

// pathToFileURL handles the Windows drive-letter form (file:///d:/...) that
// naive string concatenation gets wrong.
if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  process.exit(await main());
}
