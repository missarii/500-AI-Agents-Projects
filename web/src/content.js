import heroImage from "../../images/AIAgentUseCase.jpg";
import industryImage from "../../images/industry_usecase1.png";
import repoReadme from "../../README.md?raw";
import agentsReadme from "../../agents/README.md?raw";
import courseReadme from "../../crewai_mcp_course/README.md?raw";

const agentFiles = import.meta.glob(
  "../../agents/*/{README.md,agent.py,metadata.yaml,requirements.txt}",
  {
    eager: true,
    import: "default",
    query: "?raw",
  },
);

const courseFiles = import.meta.glob("../../crewai_mcp_course/**/*.{md,py,txt}", {
  eager: true,
  import: "default",
  query: "?raw",
});

export function stripMarkdown(value = "") {
  return String(value)
    .replace(/<[^>]*>/g, " ")
    .replace(/!\[[^\]]*]\([^)]+\)/g, " ")
    .replace(/\[([^\]]+)]\([^)]+\)/g, "$1")
    .replace(/[*_`>#]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

export function slugify(value = "item") {
  const cleaned = stripMarkdown(value)
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");

  return cleaned || "item";
}

function titleCase(value = "") {
  return stripMarkdown(value)
    .replace(/^[^A-Za-z0-9]+/, "")
    .replace(/[-_]+/g, " ")
    .split(" ")
    .filter(Boolean)
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

function formatFramework(value = "") {
  const key = slugify(value);
  const names = {
    agno: "Agno",
    autogen: "AutoGen",
    crewai: "CrewAI",
    langchain: "LangChain",
    langgraph: "LangGraph",
    llamaindex: "LlamaIndex",
    "llama-index": "LlamaIndex",
  };
  return names[key] || titleCase(value || "Python");
}

function cleanCell(value = "") {
  return stripMarkdown(value)
    .replace(/^[^A-Za-z0-9]+/, "")
    .replace(/\s+/g, " ")
    .trim();
}

function extractUrl(value = "") {
  const markdownUrls = Array.from(String(value).matchAll(/\]\((https?:\/\/[^)]+)\)/g))
    .map((match) => match[1])
    .filter((url) => !url.includes("img.shields.io"));
  if (markdownUrls.length > 0) {
    return markdownUrls[markdownUrls.length - 1];
  }

  const directUrls = String(value)
    .match(/https?:\/\/[^\s)]+/g)
    ?.filter((url) => !url.includes("img.shields.io"));
  return directUrls?.[directUrls.length - 1] || "";
