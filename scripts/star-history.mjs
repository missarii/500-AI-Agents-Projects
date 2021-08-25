  const px = (d) => PAD_L + ((d - t0) / span) * (W - PAD_L - PAD_R);
  const py = (v) => H - PAD_B - (v / top) * (H - PAD_T - PAD_B);

  const line = points.map(([d, v]) => `${px(d).toFixed(1)},${py(v).toFixed(1)}`).join(' ');
  const area = `${PAD_L},${H - PAD_B} ${line} ${px(t1).toFixed(1)},${H - PAD_B}`;

  const grid = ticks.map((t) =>
    `<line x1="${PAD_L}" y1="${py(t).toFixed(1)}" x2="${W - PAD_R}" y2="${py(t).toFixed(1)}" class="grid"/>`
  ).join('\n');

  const ylab = ticks.map((t) =>
    `<text x="${PAD_L - 10}" y="${(py(t) + 4).toFixed(1)}" class="lbl" text-anchor="end">${fmt(t)}</text>`
  ).join('\n');

  const xlab = Array.from({ length: 5 }, (_, i) => {
    const d = new Date(t0.getTime() + (t1 - t0) * (i / 4));
    return `<text x="${px(d).toFixed(1)}" y="${H - PAD_B + 22}" class="lbl" text-anchor="middle">${monthYear(d)}</text>`;
  }).join('\n');

  const stars = points[points.length - 1][1].toLocaleString('en-US');
  const updated = `${new Date().getUTCDate()} ${monthYear(new Date())}`;

  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="Star history for ${repo}">
<style>
  .bg{fill:#ffffff} .grid{stroke:#d8dee4;stroke-width:1}
  .lbl{fill:#57606a;font:12px -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
  .ttl{fill:#1f2328;font:600 14px -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
  .ln{fill:none;stroke:#ffc107;stroke-width:2.5;stroke-linejoin:round;stroke-linecap:round}
  .ar{fill:#ffc107;opacity:.15}
  @media (prefers-color-scheme: dark){
    .bg{fill:#0d1117} .grid{stroke:#30363d} .lbl{fill:#8b949e} .ttl{fill:#e6edf3}
  }
</style>
<rect width="${W}" height="${H}" class="bg"/>
${grid}
<polygon points="${area}" class="ar"/>
<polyline points="${line}" class="ln"/>
${ylab}
${xlab}
<text x="${PAD_L}" y="20" class="ttl">${repo} &#183; ${stars} stars</text>
<text x="${W - PAD_R}" y="20" class="lbl" text-anchor="end">updated ${updated}</text>
</svg>
`;
}

/** Smallest thing that fails if the maths breaks. */
function selfCheck() {
  const pts = [
    [new Date('2024-01-01T00:00:00Z'), 1],
    [new Date('2024-06-01T00:00:00Z'), 500],
    [new Date('2025-01-01T00:00:00Z'), 1000],
  ];
  const svg = renderSvg(pts, 'owner/repo');
