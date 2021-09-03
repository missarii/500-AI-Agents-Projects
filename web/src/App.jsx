    { label: "requirements.txt", path: `${agent.localPath}/requirements.txt`, content: agent.requirementsText },
    { label: "metadata.yaml", path: `${agent.localPath}/metadata.yaml`, content: agent.metadataText },
  ];
  const selected = files.find((file) => file.label === selectedFile) || files[0];
  const related = catalog.agents
    .filter((item) => item.slug !== agent.slug && item.framework === agent.framework)
    .slice(0, 3);

  return (
    <>
      <PageHero
        eyebrow={`${agent.framework} agent`}
        title={agent.title}
        description={agent.description}
        icon={GitBranch}
      />
      <section className="detail-layout">
        <aside className="detail-aside">
          <MetadataPanel agent={agent} />
          <h2>Run in 5 minutes</h2>
          <CodeBlock
            code={
              (agent.runCommands[0] || agent.setupCommands[0]) ??
              [`cd ${agent.localPath}`, "pip install -r requirements.txt", "python agent.py"].join("\n")
            }
            compact
          />
          <h2>Architecture</h2>
          <FlowTrace agent={agent} />
        </aside>
        <article className="detail-main">
          <section className="explain-panel">
            <h2>How it works</h2>
            <p>{getIntro(agent.readme, agent.description)}</p>
            <ul className="check-list">
              {(agent.features.length ? agent.features : defaultAgentSteps(agent)).map((feature) => (
                <li key={feature}>
                  <CheckCircle2 size={16} aria-hidden="true" />
                  {feature}
                </li>
              ))}
            </ul>
          </section>
          <FileTabs files={files} selected={selectedFile} onSelect={setSelectedFile} />
          <CodeBlock code={selected.content || "# File content not found"} />
          <CodeExplanation code={selected.content || ""} context={selected.label} agent={agent} />
          {related.length ? (
            <section className="related-band">
              <h2>Related {agent.framework} agents</h2>
              <div className="mini-card-grid">
                {related.map((item) => (
                  <AgentCard agent={item} key={item.id} />
                ))}
              </div>
            </section>
          ) : null}
        </article>
      </section>
    </>
  );
}

function defaultAgentSteps(agent) {
  return [
    `Loads configuration for ${agent.llm}`,
    `Creates a ${agent.framework} workflow around the core task`,
    "Accepts user input through the command line or defaults",
    "Calls tools, models, or local data helpers",
    "Returns a structured result for the user",
  ];
}

function MetadataPanel({ agent }) {
  const rows = [
    ["Path", agent.localPath],
    ["Framework", agent.framework],
    ["Difficulty", agent.difficulty],
    ["Industry", agent.industry],
    ["Model", agent.llm],
    ["Language", agent.language],
  ];

  return (
    <section className="metadata-panel">
      <h2>Project metadata</h2>
      {rows.map(([label, value]) => (
        <div className="meta-row" key={label}>
          <span>{label}</span>
          <strong>{value}</strong>
        </div>
      ))}
    </section>
  );
}

function FlowTrace({ agent }) {
  const steps =
    agent.framework === "Langgraph" || agent.framework === "LangGraph"
      ? ["Input", "State", "Node", "Tool", "Response"]
      : agent.framework === "Crewai" || agent.framework === "CrewAI"
        ? ["Goal", "Agent", "Task", "Crew", "Output"]
        : ["Input", "Planner", "Tool", "Model", "Output"];

  return (
    <div className="flow-trace">
      {steps.map((step, index) => (
        <div className="flow-step" key={step}>
          <span>{index + 1}</span>
          <strong>{step}</strong>
        </div>
      ))}
    </div>
  );
}

function UseCasesPage() {
  const [query, setQuery] = useState("");
  const [framework, setFramework] = useState("all");
  const frameworks = ["all", ...new Set(catalog.useCases.map((item) => slugify(item.framework)))];
  const useCases = catalog.useCases.filter(
    (item) =>
      matchesQuery(item, query) &&
      (framework === "all" || slugify(item.framework) === framework),
  );

  return (
    <>
      <PageHero
        eyebrow="README catalog"
        title="Dedicated page for every README use case"
        description="The catalog is parsed from the repository README tables, so each external project gets a page, source section, and redirect route."
        icon={Boxes}
      />
