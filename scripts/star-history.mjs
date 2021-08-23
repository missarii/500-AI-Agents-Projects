      Array.from({ length: samples }, (_, i) => Math.round(1 + i * step))
    )].sort((a, b) => a - b);
  }

  const points = [];
  for (const n of indices) {
    let page;
    try {
      page = await get(`${API}/repos/${repo}/stargazers?per_page=1&page=${n}`, token, STAR_JSON);
    } catch (e) {
      // GitHub caps deep pagination on some endpoints. A gap mid-curve is
      // survivable, so skip rather than abort the whole run.
      console.error(`  skip index ${n}: ${e.message}`);
      continue;
    }
    const at = page?.[0]?.starred_at;
    if (at) points.push([new Date(at), n]);
  }

  points.sort((a, b) => a[0] - b[0]);
  return points;
}

/** Round the axis maximum up to a readable step (1/2/2.5/5 x 10^n). */
export function niceTicks(hi, count = 5) {
  if (hi <= 0) return { ticks: [0], top: 1 };
  const raw = hi / count;
  const mag = 10 ** Math.floor(Math.log10(raw));
  let step = 10 * mag;
  for (const m of [1, 2, 2.5, 5, 10]) {
    if (m * mag >= raw) { step = m * mag; break; }
  }
  const top = Math.round(step * count);
  return { ticks: Array.from({ length: count + 1 }, (_, i) => Math.round(step * i)), top };
}

export function fmt(n) {
  if (n < 1000) return String(n);
  return n % 1000 === 0 ? `${n / 1000}k` : `${(n / 1000).toFixed(1)}k`;
}

const MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const monthYear = (d) => `${MONTHS[d.getUTCMonth()]} ${d.getUTCFullYear()}`;

export function renderSvg(points, repo) {
  if (!points.length) {
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}"></svg>\n`;
  }

  const t0 = points[0][0], t1 = points[points.length - 1][0];
  const span = Math.max(t1 - t0, 1);
  const { ticks, top } = niceTicks(points[points.length - 1][1]);

