  return cleanCell(markdown.match(/^#\s+(.+)$/m)?.[1] || "");
}

function extractSection(markdown = "", headingPattern) {
  const lines = markdown.split(/\r?\n/);
  const start = lines.findIndex((line) => {
    const heading = line.match(/^#{2,4}\s+(.+)$/);
    return heading && headingPattern.test(heading[1]);
  });
  if (start === -1) return "";

  const output = [];
  for (let index = start + 1; index < lines.length; index += 1) {
    if (/^#{2,4}\s+/.test(lines[index])) break;
    output.push(lines[index]);
  }
  return output.join("\n").trim();
}

function extractList(section = "", limit = 6) {
  return section
    .split(/\r?\n/)
    .map((line) => line.match(/^\s*(?:[-*]|\d+\.)\s+(.+)$/)?.[1])
    .filter(Boolean)
    .map(cleanCell)
    .filter(Boolean)
    .slice(0, limit);
}

function extractCodeFences(section = "") {
  return Array.from(section.matchAll(/```(?:bash|sh|shell)?\s*\n([\s\S]*?)```/g))
    .map((match) => match[1].trim())
    .filter(Boolean);
}

function extractPythonConcepts(code = "") {
  const functions = Array.from(code.matchAll(/^def\s+([A-Za-z_][A-Za-z0-9_]*)/gm)).map(
    (match) => match[1],
  );
  const classes = Array.from(code.matchAll(/^class\s+([A-Za-z_][A-Za-z0-9_]*)/gm)).map(
    (match) => match[1],
  );
  const signals = [
    code.includes("StateGraph") && "state graph",
    code.includes("Crew(") && "crew orchestration",
    code.includes("Agent(") && "agent roles",
    code.includes("Task(") && "task pipeline",
    code.includes("Tool") && "tool calls",
    code.includes("argparse") && "command line interface",
    code.includes("sqlite3") && "local database",
    code.includes("pandas") && "dataframe processing",
    code.includes("Tavily") && "web search",
  ].filter(Boolean);

  return {
    functions: functions.slice(0, 10),
    classes: classes.slice(0, 8),
    signals,
  };
}

function buildAgents() {
  const folders = {};
  Object.entries(agentFiles).forEach(([path, raw]) => {
    const match = path.match(/agents\/([^/]+)\/([^/]+)$/);
    if (!match) return;
    const [, folder, fileName] = match;
    folders[folder] = folders[folder] || {};
    folders[folder][fileName] = raw;
  });

  return Object.entries(folders)
    .map(([folder, files]) => {
      const metadata = parseYaml(files["metadata.yaml"] || "");
      const readme = files["README.md"] || "";
      const code = files["agent.py"] || "";
      const setupSection = extractSection(readme, /setup|installation/i);
      const runSection = extractSection(readme, /run|usage/i);
      const features =
        extractList(extractSection(readme, /what it does/i), 7).length > 0
          ? extractList(extractSection(readme, /what it does/i), 7)
          : extractList(extractSection(readme, /features|use cases/i), 7);
      const title = titleCase(firstHeading(readme) || metadata.title || folder);
      const number = folder.match(/^\d+/)?.[0] || "";
      const concepts = extractPythonConcepts(code);
