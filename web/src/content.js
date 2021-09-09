}

function splitTableRow(line = "") {
  return line
    .trim()
    .replace(/^\|/, "")
    .replace(/\|$/, "")
    .split("|")
    .map((cell) => cell.trim());
}

function isDividerRow(line = "") {
  return /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(line);
}

function getHeaderKey(header = "") {
  return stripMarkdown(header).toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
}

function inferFramework(source = "") {
  if (/crewai/i.test(source)) return "CrewAI";
  if (/autogen/i.test(source)) return "AutoGen";
  if (/agno/i.test(source)) return "Agno";
  if (/langgraph/i.test(source)) return "LangGraph";
  if (/llamaindex|llama index/i.test(source)) return "LlamaIndex";
  return "Cross-industry";
}

function isUseCaseTable(headers, sourceHeading) {
  const headerText = headers.map(getHeaderKey).join(" ");
  if (/navigation guide|framework comparison/i.test(sourceHeading)) return false;
  return (
    /description/.test(headerText) &&
    /use case|project|agent|example/.test(headerText) &&
    /code|github|notebook|link|project/.test(headerText)
  );
}

function pickRowValue(row, candidates) {
  const key = Object.keys(row).find((item) =>
    candidates.some((candidate) => item.includes(candidate)),
  );
  return key ? row[key] : "";
}

export function parseReadmeUseCases(markdown = repoReadme) {
  const lines = markdown.split(/\r?\n/);
  const records = [];
  const usedIds = new Set();
  let inFence = false;
  let h2 = "";
  let h3 = "";
  let subheading = "";

  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index];
    if (/^\s*```/.test(line)) {
      inFence = !inFence;
      continue;
    }
    if (inFence) continue;

    const heading = line.match(/^(#{2,4})\s+(.+)$/);
    if (heading) {
      const level = heading[1].length;
      const value = cleanCell(heading[2]);
      if (level === 2) {
        h2 = value;
        h3 = "";
        subheading = "";
      } else if (level === 3) {
        h3 = value;
        subheading = "";
      } else {
        subheading = value;
      }
      continue;
    }

    const boldHeading = line.match(/^\*\*([^*]+)\*\*\s*$/);
    if (boldHeading) {
      subheading = cleanCell(boldHeading[1]);
      continue;
    }

    if (!line.trim().startsWith("|") || !lines[index + 1] || !isDividerRow(lines[index + 1])) {
