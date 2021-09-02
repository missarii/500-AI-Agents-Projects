        <img src={catalog.images.hero} alt="AI agent use case map" />
        <div>
          <p className="eyebrow">Live catalog</p>
          <h2>Search every local agent and README table row</h2>
          <SearchPanel compact />
        </div>
      </section>

      <section className="content-band">
        <SectionHeader
          eyebrow="Runnable code"
          title="Local agent implementations"
          action={{ label: "View all agents", href: "/agents" }}
        />
        <div className="card-grid">
          {featuredAgents.map((agent) => (
            <AgentCard agent={agent} key={agent.id} />
          ))}
        </div>
      </section>

      <section className="content-band">
        <SectionHeader
          eyebrow="README use cases"
          title="External projects with dedicated pages"
          action={{ label: "View all use cases", href: "/use-cases" }}
        />
        <div className="usecase-grid">
          {featuredUseCases.map((useCase) => (
            <UseCaseCard useCase={useCase} key={useCase.id} />
          ))}
        </div>
      </section>

      <FrameworkStrip />
    </>
  );
}

function SectionHeader({ eyebrow, title, action }) {
  return (
    <div className="section-header">
      <div>
        <p className="eyebrow">{eyebrow}</p>
        <h2>{title}</h2>
      </div>
      {action ? (
        <a className="inline-action" href={pathFor(action.href)}>
          {action.label} <ArrowRight size={16} aria-hidden="true" />
        </a>
      ) : null}
    </div>
  );
}

function CourseRail() {
  return (
    <div className="course-rail">
      {catalog.courseLessons.map((lesson) => (
        <a className="lesson-row" href={pathFor(`/course/${lesson.slug}`)} key={lesson.slug}>
          <span>{lesson.number}</span>
          <div>
            <strong>{lesson.title}</strong>
            <small>{lesson.summary}</small>
          </div>
          <ArrowRight size={16} aria-hidden="true" />
        </a>
      ))}
    </div>
  );
}

function FrameworkStrip() {
  return (
    <section className="content-band">
      <SectionHeader
        eyebrow="Decision support"
        title="Framework map"
        action={{ label: "Compare frameworks", href: "/frameworks" }}
      />
      <div className="framework-grid">
        {catalog.frameworks.map((framework) => (
          <a
            className={`framework-card tone-${framework.accent}`}
            href={pathFor(`/frameworks/${framework.slug}`)}
            key={framework.slug}
          >
            <strong>{framework.name}</strong>
            <p>{framework.bestFor}</p>
            <span>{framework.decision}</span>
          </a>
        ))}
      </div>
    </section>
  );
}

function AgentCard({ agent }) {
  return (
    <a className="agent-card" href={pathFor(`/agents/${agent.slug}`)}>
      <div className="card-topline">
        <span className={`framework-pill ${slugify(agent.framework)}`}>{agent.framework}</span>
        <small>{agent.difficulty}</small>
      </div>
      <h3>{agent.title}</h3>
      <p>{agent.description}</p>
      <div className="tag-list">
        {[agent.industry, agent.llm, ...agent.tags].filter(Boolean).slice(0, 4).map((tag) => (
          <span key={tag}>{tag}</span>
        ))}
      </div>
    </a>
  );
}

function UseCaseCard({ useCase }) {
  return (
    <article className="usecase-card">
      <div className="card-topline">
        <span className={`framework-pill ${slugify(useCase.framework)}`}>{useCase.framework}</span>
        <small>{useCase.resourceType}</small>
      </div>
      <h3>{useCase.title}</h3>
      <p>{useCase.description}</p>
      <div className="card-actions">
        <a href={pathFor(`/use-cases/${useCase.id}`)}>
          <FileText size={15} aria-hidden="true" />
          Detail
        </a>
        {useCase.url ? (
          <a href={pathFor(`/go/${useCase.id}`)}>
            <ExternalLink size={15} aria-hidden="true" />
