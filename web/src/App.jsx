  const visibleFrameworks = selected ? [selected] : catalog.frameworks;

  return (
    <>
      <PageHero
        eyebrow="Frameworks"
        title={selected ? selected.name : "Choose the right agent framework"}
        description={
          selected
            ? selected.decision
            : "Compare the main framework families represented in this repository, then jump into matching agents and examples."
        }
        icon={Workflow}
      />
      <section className="content-band">
        <div className="framework-grid">
          {visibleFrameworks.map((framework) => {
            const agents = catalog.agents.filter(
              (agent) => slugify(agent.framework) === framework.slug,
            );
            const useCases = catalog.useCases.filter(
              (useCase) => slugify(useCase.framework) === framework.slug,
            );
            return (
              <article className={`framework-detail tone-${framework.accent}`} key={framework.slug}>
                <div>
                  <h2>{framework.name}</h2>
                  <p>{framework.bestFor}</p>
                  <span>{framework.decision}</span>
                </div>
                <div className="framework-stats">
                  <strong>{agents.length}</strong>
                  <span>local agents</span>
                  <strong>{useCases.length}</strong>
                  <span>README use cases</span>
                </div>
                <a className="inline-action" href={pathFor(`/frameworks/${framework.slug}`)}>
                  Open framework <ArrowRight size={16} aria-hidden="true" />
                </a>
              </article>
            );
          })}
        </div>
      </section>
      {selected ? (
        <section className="content-band">
          <SectionHeader eyebrow={selected.name} title="Matching examples" />
          <div className="card-grid">
            {catalog.agents
              .filter((agent) => slugify(agent.framework) === selected.slug)
              .slice(0, 6)
              .map((agent) => (
                <AgentCard agent={agent} key={agent.id} />
              ))}
          </div>
        </section>
      ) : null}
    </>
  );
}

function CatalogToolbar({ query, onQuery, filters, filter, onFilter }) {
  return (
    <section className="catalog-toolbar">
      <label className="search-box">
        <Search size={18} aria-hidden="true" />
        <input
          value={query}
          onChange={(event) => onQuery(event.target.value)}
          placeholder="Search catalog"
        />
      </label>
      <div className="filter-row" aria-label="Framework filter">
        <Filter size={17} aria-hidden="true" />
        {filters.map((item) => (
          <button
            className={filter === item ? "active" : ""}
            onClick={() => onFilter(item)}
            type="button"
            key={item}
          >
            {item === "all" ? "All" : catalog.frameworks.find((fw) => fw.slug === item)?.name || item}
          </button>
        ))}
      </div>
    </section>
  );
}

function PageHero({ eyebrow, title, description, icon: Icon, action }) {
  return (
    <section className="page-hero">
      <div>
        <p className="eyebrow">{eyebrow}</p>
        <h1>{title}</h1>
        <p>{description}</p>
        {action ? (
          <a
            className="primary-action"
            href={action.external ? action.href : pathFor(action.href)}
            rel={action.external ? "noreferrer" : undefined}
          >
            <ExternalLink size={18} aria-hidden="true" />
            {action.label}
          </a>
        ) : null}
      </div>
      <div className="page-hero-icon" aria-hidden="true">
        <Icon size={42} />
      </div>
    </section>
  );
}

function FileTabs({ files, selected, onSelect }) {
  return (
    <div className="file-tabs" role="tablist" aria-label="Files">
      {files.map((file) => (
        <button
          className={selected === file.label ? "active" : ""}
          key={file.label}
          onClick={() => onSelect(file.label)}
          type="button"
        >
          <FileText size={15} aria-hidden="true" />
          {file.label}
        </button>
      ))}
    </div>
  );
}

