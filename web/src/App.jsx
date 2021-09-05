      <CatalogToolbar query={query} onQuery={setQuery} filters={frameworks} filter={framework} onFilter={setFramework} />
      <section className="content-band">
        <div className="catalog-count">{useCases.length} matching use cases</div>
        <div className="usecase-grid">
          {useCases.map((useCase) => (
            <UseCaseCard useCase={useCase} key={useCase.id} />
          ))}
        </div>
      </section>
    </>
  );
}

function UseCasePage({ useCase }) {
  const relatedAgents = catalog.agents
    .filter(
      (agent) =>
        slugify(agent.framework) === slugify(useCase.framework) ||
        slugify(agent.industry) === slugify(useCase.industry),
    )
    .slice(0, 4);
  const relatedCases = catalog.useCases
    .filter((item) => item.id !== useCase.id && item.framework === useCase.framework)
    .slice(0, 4);

  return (
    <>
      <PageHero
        eyebrow={useCase.sourceHeading}
        title={useCase.title}
        description={useCase.description}
        icon={ExternalLink}
      />
      <section className="detail-layout">
        <aside className="detail-aside">
          <section className="metadata-panel">
            <h2>Use case metadata</h2>
            <div className="meta-row">
              <span>Framework</span>
              <strong>{useCase.framework}</strong>
            </div>
            <div className="meta-row">
              <span>Industry</span>
              <strong>{useCase.industry}</strong>
            </div>
            <div className="meta-row">
              <span>Source</span>
              <strong>{useCase.sourceHeading}</strong>
            </div>
            <div className="meta-row">
              <span>Resource</span>
              <strong>{useCase.resourceType}</strong>
            </div>
          </section>
          {useCase.url ? (
            <a className="primary-action full-width" href={pathFor(`/go/${useCase.id}`)}>
              <ExternalLink size={18} aria-hidden="true" />
              Open redirect
            </a>
          ) : null}
        </aside>
        <article className="detail-main">
          <section className="explain-panel">
            <h2>What this adds</h2>
            <p>
              This page turns a README table row into a durable catalog entry with context,
              framework grouping, industry filtering, and a redirect route for the source project.
            </p>
            <div className="source-block">
              <strong>{useCase.title}</strong>
              <span>{useCase.description}</span>
              {useCase.url ? <code>{useCase.url}</code> : null}
            </div>
          </section>
          {relatedAgents.length ? (
            <section className="related-band">
              <h2>Related local agents</h2>
              <div className="mini-card-grid">
                {relatedAgents.map((agent) => (
                  <AgentCard agent={agent} key={agent.id} />
                ))}
              </div>
            </section>
          ) : null}
          {relatedCases.length ? (
            <section className="related-band">
              <h2>Similar use cases</h2>
              <div className="usecase-grid compact-grid">
                {relatedCases.map((item) => (
                  <UseCaseCard useCase={item} key={item.id} />
                ))}
              </div>
            </section>
          ) : null}
        </article>
      </section>
    </>
  );
}

function RedirectPage({ useCase }) {
  useEffect(() => {
    if (!useCase?.url) return undefined;
    const timer = window.setTimeout(() => {
      window.location.href = useCase.url;
    }, 900);
    return () => window.clearTimeout(timer);
  }, [useCase]);

  if (!useCase) return <NotFound />;

  return (
    <PageHero
      eyebrow="Redirect"
      title={useCase.title}
      description={`Opening ${useCase.url || "the source project"}.`}
      icon={ExternalLink}
      action={
        useCase.url
          ? {
              label: "Open now",
              href: useCase.url,
              external: true,
            }
          : null
      }
    />
  );
}

function FrameworksPage({ frameworkSlug }) {
  const selected = catalog.frameworks.find((item) => item.slug === frameworkSlug);
