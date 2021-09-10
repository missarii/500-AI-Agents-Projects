  },
  {
    slug: "lesson-03",
    number: "03",
    title: "CrewAI With FastMCP-Style Tools",
    summary:
      "Use a FastMCP-style tool surface to let CrewAI agents query structured project data and produce a status report.",
    files: [
      {
        label: "agent.py",
        path: "crewai_mcp_course/lesson_03/agent.py",
        content: getCourseFile("lesson_03/agent.py"),
      },
      {
        label: "mcp_server.py",
        path: "crewai_mcp_course/lesson_03/mcp_server.py",
        content: getCourseFile("lesson_03/mcp_server.py"),
      },
      {
        label: "requirements.txt",
        path: "crewai_mcp_course/lesson_03/requirements.txt",
        content: getCourseFile("lesson_03/requirements.txt"),
      },
    ],
    objectives: [
      "Model a tool contract that resembles MCP server access",
      "Let agents request project records through tools",
      "Generate a management-ready project status report",
      "See how MCP-style boundaries improve agent design",
    ],
    runCommands: ["cd crewai_mcp_course/lesson_03", "pip install -r requirements.txt", "python agent.py"],
  },
];

export const frameworks = [
  {
    slug: "langgraph",
    name: "LangGraph",
    accent: "cyan",
    bestFor: "Stateful workflows, graph control, retries, RAG, and production routing.",
    decision: "Choose it when the agent needs explicit state transitions and reliable recovery paths.",
  },
  {
    slug: "crewai",
    name: "CrewAI",
    accent: "green",
    bestFor: "Role-based teams, business automation, repeatable task handoffs, and fast prototypes.",
    decision: "Choose it when the project maps naturally to specialists with goals and tasks.",
  },
  {
    slug: "autogen",
    name: "AutoGen",
    accent: "amber",
    bestFor: "Code generation, research collaboration, feedback loops, and executable experiments.",
    decision: "Choose it when agents need to talk, critique, run code, and iterate.",
  },
  {
    slug: "agno",
    name: "Agno",
    accent: "rose",
    bestFor: "Lightweight tool agents, quick iteration, model flexibility, and compact apps.",
    decision: "Choose it when you want a focused tool-calling agent with low ceremony.",
  },
  {
    slug: "llamaindex",
    name: "LlamaIndex",
    accent: "violet",
    bestFor: "Document Q&A, enterprise retrieval, data connectors, and knowledge workflows.",
    decision: "Choose it when the data pipeline matters as much as the agent behavior.",
  },
];

export const catalog = {
  repoReadme,
  agentsReadme,
  courseReadme,
  agents: buildAgents(),
  useCases: parseReadmeUseCases(repoReadme),
  courseLessons,
  frameworks,
  images: {
    hero: heroImage,
    industry: industryImage,
  },
};
