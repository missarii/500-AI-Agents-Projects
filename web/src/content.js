      continue;
    }

    const headers = splitTableRow(line);
    const sourceHeading = [h2, h3, subheading].filter(Boolean).join(" / ");
    if (!isUseCaseTable(headers, sourceHeading)) {
      continue;
    }

    index += 2;
    while (index < lines.length && lines[index].trim().startsWith("|")) {
      const cells = splitTableRow(lines[index]);
      if (cells.length >= headers.length - 1) {
        const row = {};
        headers.forEach((header, cellIndex) => {
          row[getHeaderKey(header)] = cells[cellIndex] || "";
        });

        const title =
          cleanCell(pickRowValue(row, ["use case", "project", "agent", "example"])) ||
          cleanCell(cells[0]);
        const description = cleanCell(pickRowValue(row, ["description", "best for"]));
        const industry = cleanCell(pickRowValue(row, ["industry", "domain", "category"]));
        const url = extractUrl(cells.join(" "));

        if (title && description) {
          const baseId = slugify(`${sourceHeading}-${title}`);
          let id = baseId;
          let suffix = 2;
          while (usedIds.has(id)) {
            id = `${baseId}-${suffix}`;
            suffix += 1;
          }
          usedIds.add(id);

          records.push({
            id,
            title,
            description,
            industry: industry || "General",
            framework: inferFramework(sourceHeading),
            sourceHeading,
            sourceGroup: h2,
            sourceSubheading: [h3, subheading].filter(Boolean).join(" / "),
            url,
            resourceType: /notebook|ipynb/i.test(url) ? "Notebook" : "Code",
            tags: [
              inferFramework(sourceHeading),
              industry || "General",
              h2,
              h3,
              subheading,
            ].filter(Boolean),
          });
        }
      }
      index += 1;
    }
    index -= 1;
  }

  return records;
}

function parseYaml(raw = "") {
  const data = {};
  raw.split(/\r?\n/).forEach((line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#") || !trimmed.includes(":")) return;
    const [key, ...rest] = trimmed.split(":");
    const value = rest.join(":").trim();
    if (value.startsWith("[") && value.endsWith("]")) {
      data[key.trim()] = value
        .slice(1, -1)
        .split(",")
        .map((item) => item.trim().replace(/^["']|["']$/g, ""))
        .filter(Boolean);
    } else {
      data[key.trim()] = value.replace(/^["']|["']$/g, "");
    }
  });
  return data;
}

function firstHeading(markdown = "") {
