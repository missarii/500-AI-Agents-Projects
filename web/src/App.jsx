        return (
          <article className="stat-tile" key={stat.label}>
            <Icon size={18} aria-hidden="true" />
            <strong>{stat.value}</strong>
            <span>{stat.label}</span>
          </article>
        );
      })}
    </section>
  );
}

function GraphHero() {
  const nodes = [
    { label: "CrewAI course", path: "/course", x: 11, y: 22, tone: "green" },
    { label: "Runnable agents", path: "/agents", x: 52, y: 13, tone: "cyan" },
    { label: "Use cases", path: "/use-cases", x: 74, y: 48, tone: "amber" },
    { label: "Frameworks", path: "/frameworks", x: 24, y: 65, tone: "rose" },
    { label: "Code pages", path: "/agents/01-web-research-agent", x: 54, y: 78, tone: "violet" },
  ];

  return (
    <section className="hero-grid">
      <div className="hero-copy">
        <p className="eyebrow">Course front page plus project atlas</p>
        <h1>500+ AI Agent Projects</h1>
        <p>
          A premium React atlas for learning, browsing, running, and redirecting into the
          strongest AI agent examples in this repository.
        </p>
        <div className="hero-actions">
          <a className="primary-action" href={pathFor("/course")}>
            <GraduationCap size={18} aria-hidden="true" />
            Start course
          </a>
          <a className="secondary-action" href={pathFor("/use-cases")}>
            <Search size={18} aria-hidden="true" />
            Browse use cases
          </a>
        </div>
      </div>

      <div className="graph-stage" aria-label="Interactive agent atlas graph">
        <svg className="edge-layer" viewBox="0 0 100 100" preserveAspectRatio="none">
          <path className="graph-edge edge-one" d="M12 25 C30 8, 42 12, 52 16" />
          <path className="graph-edge edge-two" d="M54 18 C69 23, 78 33, 75 50" />
          <path className="graph-edge edge-three" d="M72 51 C61 71, 51 78, 27 67" />
          <path className="graph-edge edge-four" d="M25 65 C12 54, 8 38, 12 25" />
          <path className="graph-edge edge-five" d="M53 17 C48 39, 48 60, 54 78" />
        </svg>
        {nodes.map((node) => (
          <a
            className={`graph-node tone-${node.tone}`}
            href={pathFor(node.path)}
            key={node.label}
            style={{ left: `${node.x}%`, top: `${node.y}%` }}
          >
            <span />
            {node.label}
          </a>
        ))}
        <div className="graph-console">
          <span>agent_state</span>
          <strong>ready</strong>
          <small>nodes: {catalog.agents.length + catalog.frameworks.length}</small>
        </div>
      </div>
    </section>
  );
}

function SearchPanel({ compact = false }) {
  const [query, setQuery] = useState("");
  const agentMatches = catalog.agents.filter((agent) => matchesQuery(agent, query)).slice(0, 4);
  const useCaseMatches = catalog.useCases.filter((useCase) => matchesQuery(useCase, query)).slice(0, 6);

  return (
    <section className={compact ? "search-panel compact" : "search-panel"}>
      <label className="search-box">
        <Search size={18} aria-hidden="true" />
        <input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search agents, use cases, frameworks, industries"
        />
      </label>

      <div className="search-results">
        {[...agentMatches, ...useCaseMatches].map((item) => {
          const isAgent = Boolean(item.localPath);
          return (
            <a
              className="result-row"
              href={pathFor(isAgent ? `/agents/${item.slug}` : `/use-cases/${item.id}`)}
              key={`${isAgent ? "agent" : "case"}-${item.id}`}
            >
              <span className={`mini-dot ${slugify(item.framework)}`} />
              <strong>{item.title}</strong>
              <small>{isAgent ? item.localPath : item.sourceHeading}</small>
            </a>
          );
        })}
      </div>
    </section>
  );
}

function HomePage() {
  const featuredAgents = catalog.agents.slice(0, 6);
  const featuredUseCases = catalog.useCases.slice(0, 8);

  return (
    <>
      <GraphHero />
      <StatStrip />

      <section className="split-section">
        <div className="section-copy">
          <p className="eyebrow">Start here</p>
          <h2>CrewAI with FastMCP-style lessons at the front</h2>
          <p>
            The course is the guided entry point, then the atlas opens into local code agents
            and README-linked external examples.
          </p>
          <a className="inline-action" href={pathFor("/course")}>
            Open course page <ArrowRight size={16} aria-hidden="true" />
          </a>
        </div>
        <CourseRail />
      </section>

      <section className="media-band">
