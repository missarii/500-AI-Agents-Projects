            Redirect
          </a>
        ) : null}
      </div>
    </article>
  );
}

function CoursePage() {
  return (
    <>
      <PageHero
        eyebrow="Course"
        title="CrewAI with FastMCP-style integration"
        description={getIntro(catalog.courseReadme, "A practical course for building CrewAI workflows with MCP-style tool boundaries.")}
        icon={GraduationCap}
      />
      <section className="split-section">
        <div className="section-copy">
          <h2>Learning path</h2>
          <p>
            Each lesson has its own page with objectives, run commands, code files, and a code
            walkthrough surface.
          </p>
          <div className="command-stack">
            <CodeBlock
              code={[
                "cd crewai_mcp_course/lesson_01",
                "pip install -r requirements.txt",
                "python agent.py",
              ].join("\n")}
              compact
            />
          </div>
        </div>
        <CourseRail />
      </section>
      <section className="content-band">
        <SectionHeader eyebrow="Lessons" title="Separate lesson pages" />
        <div className="lesson-grid">
          {catalog.courseLessons.map((lesson) => (
            <a className="lesson-card" href={pathFor(`/course/${lesson.slug}`)} key={lesson.slug}>
              <span>{lesson.number}</span>
              <h3>{lesson.title}</h3>
              <p>{lesson.summary}</p>
              <ul>
                {lesson.objectives.slice(0, 3).map((objective) => (
                  <li key={objective}>
                    <CheckCircle2 size={15} aria-hidden="true" />
                    {objective}
                  </li>
                ))}
              </ul>
            </a>
          ))}
        </div>
      </section>
    </>
  );
}

function LessonPage({ lesson }) {
  const [selectedFile, setSelectedFile] = useState(lesson.files[0]?.label || "");
  const file = lesson.files.find((item) => item.label === selectedFile) || lesson.files[0];

  return (
    <>
      <PageHero
        eyebrow={`Lesson ${lesson.number}`}
        title={lesson.title}
        description={lesson.summary}
        icon={BookOpen}
      />
      <section className="detail-layout">
        <aside className="detail-aside">
          <h2>Objectives</h2>
          <ul className="check-list">
            {lesson.objectives.map((objective) => (
              <li key={objective}>
                <CheckCircle2 size={16} aria-hidden="true" />
                {objective}
              </li>
            ))}
          </ul>
          <h2>Run</h2>
          <CodeBlock code={lesson.runCommands.join("\n")} compact />
        </aside>
        <article className="detail-main">
          <FileTabs files={lesson.files} selected={selectedFile} onSelect={setSelectedFile} />
          <CodeBlock code={file?.content || "# File content not found"} />
          <CodeExplanation code={file?.content || ""} context="lesson" />
        </article>
      </section>
    </>
  );
}

function AgentsPage() {
  const [query, setQuery] = useState("");
  const [framework, setFramework] = useState("all");
  const frameworks = ["all", ...new Set(catalog.agents.map((agent) => slugify(agent.framework)))];
  const agents = catalog.agents.filter(
    (agent) =>
      matchesQuery(agent, query) &&
      (framework === "all" || slugify(agent.framework) === framework),
  );

  return (
    <>
      <PageHero
        eyebrow="Runnable agents"
        title="Local code pages for every implementation"
        description="Each agent page explains the framework, setup, run commands, architecture, and code structure from the files in agents/."
        icon={Code2}
      />
      <CatalogToolbar query={query} onQuery={setQuery} filters={frameworks} filter={framework} onFilter={setFramework} />
      <section className="content-band">
        <div className="card-grid">
          {agents.map((agent) => (
            <AgentCard agent={agent} key={agent.id} />
          ))}
        </div>
      </section>
    </>
  );
}

function AgentPage({ agent }) {
  const [selectedFile, setSelectedFile] = useState("agent.py");
  const files = [
    { label: "agent.py", path: `${agent.localPath}/agent.py`, content: agent.code },
    { label: "README.md", path: `${agent.localPath}/README.md`, content: agent.readme },
