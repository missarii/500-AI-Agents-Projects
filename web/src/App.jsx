function CodeBlock({ code, compact = false }) {
  const [copied, setCopied] = useState(false);
  const copy = async () => {
    await navigator.clipboard?.writeText(code);
    setCopied(true);
    window.setTimeout(() => setCopied(false), 1200);
  };

  return (
    <div className={compact ? "code-block compact" : "code-block"}>
      <div className="code-toolbar">
        <span>
          <Terminal size={15} aria-hidden="true" />
          code
        </span>
        <button onClick={copy} type="button">
          <Copy size={14} aria-hidden="true" />
          {copied ? "Copied" : "Copy"}
        </button>
      </div>
      <pre>
        <code>{code}</code>
      </pre>
    </div>
  );
}

function CodeExplanation({ code, context, agent }) {
  const lines = code.split(/\r?\n/).filter(Boolean);
  const imports = lines.filter((line) => /^import\s|^from\s/.test(line)).slice(0, 6);
  const functions = Array.from(code.matchAll(/^def\s+([A-Za-z_][A-Za-z0-9_]*)/gm)).map(
    (match) => match[1],
  );
  const classes = Array.from(code.matchAll(/^class\s+([A-Za-z_][A-Za-z0-9_]*)/gm)).map(
    (match) => match[1],
  );

  return (
    <section className="code-explain">
      <h2>Code walkthrough</h2>
      <div className="walkthrough-grid">
        <WalkthroughCard
          icon={Layers3}
          title="Imports"
          items={imports.length ? imports : ["No import block in this file section."]}
        />
        <WalkthroughCard
          icon={Zap}
          title="Functions"
          items={functions.length ? functions.slice(0, 8) : ["No top-level functions detected."]}
        />
        <WalkthroughCard
          icon={Network}
          title="Classes"
          items={classes.length ? classes.slice(0, 6) : ["No classes detected."]}
        />
        <WalkthroughCard
          icon={Play}
          title="Role"
          items={[
            context === "agent.py"
              ? `Entrypoint for ${agent?.framework || "the"} implementation.`
              : `Reference file for ${context}.`,
            `${lines.length} non-empty lines are bundled into this page.`,
          ]}
        />
      </div>
    </section>
  );
}

function WalkthroughCard({ icon: Icon, title, items }) {
  return (
    <article className="walk-card">
      <Icon size={18} aria-hidden="true" />
      <h3>{title}</h3>
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </article>
  );
}

function NotFound() {
  return (
    <PageHero
      eyebrow="Missing page"
      title="This atlas page was not found"
      description="The catalog route does not match a local agent, lesson, use case, or framework."
      icon={Search}
      action={{ label: "Back to atlas", href: "/" }}
    />
  );
}

function App() {
  const route = useHashRoute();
  const segments = useMemo(() => route.split("?")[0].split("/").filter(Boolean), [route]);

  let page;
  if (segments.length === 0) {
    page = <HomePage />;
  } else if (segments[0] === "course" && segments.length === 1) {
    page = <CoursePage />;
  } else if (segments[0] === "course") {
    const lesson = catalog.courseLessons.find((item) => item.slug === segments[1]);
    page = lesson ? <LessonPage lesson={lesson} /> : <NotFound />;
  } else if (segments[0] === "agents" && segments.length === 1) {
    page = <AgentsPage />;
  } else if (segments[0] === "agents") {
    const agent = catalog.agents.find((item) => item.slug === segments[1]);
    page = agent ? <AgentPage agent={agent} /> : <NotFound />;
  } else if (segments[0] === "use-cases" && segments.length === 1) {
    page = <UseCasesPage />;
  } else if (segments[0] === "use-cases") {
    const useCase = catalog.useCases.find((item) => item.id === segments[1]);
    page = useCase ? <UseCasePage useCase={useCase} /> : <NotFound />;
  } else if (segments[0] === "go") {
    const useCase = catalog.useCases.find((item) => item.id === segments[1]);
    page = <RedirectPage useCase={useCase} />;
  } else if (segments[0] === "frameworks") {
    page = <FrameworksPage frameworkSlug={segments[1]} />;
  } else {
    page = <NotFound />;
  }

  return <Shell route={route}>{page}</Shell>;
}

export default App;
