    writer = Agent(
        role="Social Media Copywriter",
        goal="Write engaging, platform-optimized content that drives engagement",
        backstory="Viral content creator with expertise in platform-specific formats, hashtags, and hooks.",
        llm=llm,
        verbose=False,
    )

    strategy_task = Task(
        description=f"""Analyze this topic for social media: "{topic}"
Brand: {brand or 'Not specified'}
Platforms: {', '.join(platforms)}
Define: core message, target audience, emotional hook, 5 relevant hashtags.""",
        agent=strategist,
        expected_output="Content strategy: message, audience, hook, and hashtags",
    )

    writing_task = Task(
        description=f"""Write social media posts for: {', '.join(platforms)}
Topic: {topic}. Brand: {brand or 'General'}.

For each platform:
- Twitter/X: 2 tweet variations (under 280 chars each) + thread opener
- LinkedIn: Professional post (150-200 words) with storytelling hook
- Instagram: Caption (100-150 words) + 15 hashtags

Make them platform-native — Twitter punchy, LinkedIn thoughtful, Instagram visual.""",
        agent=writer,
        expected_output="Platform-optimized posts for all requested platforms",
        context=[strategy_task],
    )
