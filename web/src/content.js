
      return {
        id: folder,
        slug: folder,
        number,
        title,
        description: metadata.description || cleanCell(readme.split(/\r?\n/)[2] || ""),
        framework: formatFramework(metadata.framework || "Python"),
        llm: metadata.llm || "Configurable",
        industry: titleCase(metadata.industry || "General"),
        difficulty: titleCase(metadata.difficulty || "Intermediate"),
        tags: Array.isArray(metadata.tags) ? metadata.tags : [],
        language: titleCase(metadata.language || "Python"),
        localPath: `agents/${folder}`,
        entrypoint: metadata.entrypoint || "agent.py",
        requirements: metadata.requirements || "requirements.txt",
        readme,
        code,
        requirementsText: files["requirements.txt"] || "",
        metadataText: files["metadata.yaml"] || "",
        features,
        setupCommands: extractCodeFences(setupSection),
        runCommands: extractCodeFences(runSection),
        concepts,
      };
    })
    .sort((a, b) => a.slug.localeCompare(b.slug, undefined, { numeric: true }));
}

function getCourseFile(pathSuffix) {
  const entry = Object.entries(courseFiles).find(([path]) => path.endsWith(pathSuffix));
  return entry ? entry[1] : "";
}

const courseLessons = [
  {
    slug: "lesson-01",
    number: "01",
    title: "First CrewAI Researcher",
    summary:
      "Build a single researcher agent, give it a clear role, run one task, and inspect the response path.",
    files: [
      {
        label: "agent.py",
        path: "crewai_mcp_course/lesson_01/agent.py",
        content: getCourseFile("lesson_01/agent.py"),
      },
      {
        label: "requirements.txt",
        path: "crewai_mcp_course/lesson_01/requirements.txt",
        content: getCourseFile("lesson_01/requirements.txt"),
      },
    ],
    objectives: [
      "Install the CrewAI lesson dependencies",
      "Define a role-driven research agent",
      "Attach the agent to one clear task",
      "Run the crew and read the final output",
    ],
    runCommands: ["cd crewai_mcp_course/lesson_01", "pip install -r requirements.txt", "python agent.py"],
  },
  {
    slug: "lesson-02",
    number: "02",
    title: "Multi-Agent Research Crew",
    summary:
      "Split research, writing, and editing responsibilities into a sequential CrewAI workflow.",
    files: [
      {
        label: "agent.py",
        path: "crewai_mcp_course/lesson_02/agent.py",
        content: getCourseFile("lesson_02/agent.py"),
      },
      {
        label: "requirements.txt",
        path: "crewai_mcp_course/lesson_02/requirements.txt",
        content: getCourseFile("lesson_02/requirements.txt"),
      },
    ],
    objectives: [
      "Create multiple specialist agents",
      "Connect tasks into a sequential process",
      "Pass context from researcher to writer to editor",
      "Understand where tools fit into CrewAI",
    ],
    runCommands: ["cd crewai_mcp_course/lesson_02", "pip install -r requirements.txt", "python agent.py"],
