---
lang: en-US
title: Conference Poster Sheets
description: The EasyChair and Curious spreadsheet formats Posters.science reads when you share a batch of conference posters
head:
  - - meta
    - name: og:image
      content: https://kalai.fairdataihub.org/api/generate?title=Posters.science%20Documentation&description=Conference%20Poster%20Sheets&app=posters-science&org=fairdataihub
---

# Conference Poster Sheets

When you share a batch of posters from a conference, you can add the spreadsheet your conference platform already has for them. Posters.science reads the titles, authors, affiliations, abstracts and keywords from it, so there is less to check and type by hand.

The sheet is optional. If you don't have one, share the posters as usual and their details are read from the poster files. You never need to download a sheet and fill it in.

## Adding a sheet

1. Add your poster files to the poster upload area.
2. Below it, choose your conference platform from the format menu: **EasyChair** (the default) or **Curious**.
3. Drop the sheet into the sheet upload area below the menu.

Not every conference platform is supported yet. If your sheet comes from somewhere else, share the posters without it and let us know through the [contact form](https://tally.so/r/RG8Avd) so we can add your format.

If the sheet doesn't match the format you chose, it is refused with a message naming the columns it is missing. When the sheet is the other supported format, the message tells you which one to choose.

## What the sheet changes

Anything the sheet gives takes priority over what is read from the poster file. What the sheet leaves empty is filled from the poster.

- **Title, abstract, keywords:** a filled cell replaces what was read from the poster.
- **Authors:** when the sheet lists a poster's authors, that list is used. A missing ORCID iD or affiliation for one of those authors is filled from the poster when it clearly names the same person.
- **Links:** a website or source code link in the sheet becomes a related resource of the poster.
- **Posters without a row:** a poster that no row in the sheet belongs to keeps the details read from its file.

The only changes made to sheet values are cleanup: extra spaces, placeholder words such as `n/a` or `no`, a poster number in front of the title, and affiliation numbers after author names.

## How rows find their posters

Each row in the sheet has to be linked to one of your poster files. Posters.science tries these in order:

1. **A file name column.** A column with the poster's file name (`12_smith.pdf`) links each row exactly. This is the most reliable way, so add one if you can.
2. **The submission number in the file name.** A file named by its number (`17.pdf`, `17_smith.pdf` or `bosc2026_submission_17.pdf`) links to row 17. This is how EasyChair names the files in its submissions download.
3. **The title.** Rows still without a file are matched to posters by title, with the authors as a tiebreaker, once the posters have been read.

Every link is checked against the title read from the poster. A row that doesn't seem to belong to its poster is flagged for you to look at before anything is published.

## EasyChair

Use the submissions download from EasyChair, as an Excel workbook or as CSV files.

**Excel:** the basic submissions download (one sheet), or the Conference data download (a workbook with Submissions and Authors sheets).

**CSV:** drop the files together: `submission.csv`, plus `author.csv`, `submission_topic.csv` and `topics.csv` when you have them. Only `submission.csv` is required.

### Required columns

The submissions sheet must have these columns. Other columns are fine, and header case doesn't matter.

| Column | Used for |
|--------|----------|
| `#` | The submission number, to link rows to files named by number |
| `Title` | Poster title |
| `Authors` | Author names, when there is no Authors sheet or `author.csv` |
| `Submitted` | Not stored |
| `Last updated` | Not stored |
| `Keywords` | Keywords, one per line |
| `Decision` | Only accepted submissions are kept |
| `Abstract` | Abstract |

### Columns used when present

| Column or file | Used for |
|----------------|----------|
| `Track name` | Added to the keywords |
| `Deleted` | Deleted submissions are left out |
| `Form fields` | See below |
| Authors sheet or `author.csv` | Authors in order, with first and last name, affiliation, and an ORCID iD when the web page is an orcid.org link |
| `submission_topic.csv` and `topics.csv` | Topics are added to the keywords. Topic group headings are left out |

### Rows that are left out

- Submissions marked deleted.
- Submissions whose decision is not an accept (rejected, declined, withdrawn or cancelled), once at least one submission has been accepted.
- Submissions whose submission type form field says TALK ONLY.

### Form fields

Form fields hold your conference's own questions. Only these are used:

- A DOI of a previously published abstract becomes a related resource of the poster.
- A source code link becomes a related resource of the poster.

All other answers, such as fees, diversity questions or comments for the chairs, are dropped when the file is read and never stored or shown.

Email addresses and countries from the Authors sheet are not stored either.

## Curious

Use the poster information sheet from Curious, as an `.xlsx` or `.csv` file.

### Required columns

| Column | Used for |
|--------|----------|
| `Position` | The poster's number, to link rows to files named by number |
| `Track` | Added to the keywords |
| `Title` | Poster title. A number in front (`12 - Title`) is removed when it is the poster's position |
| `Authors` | Author names, with affiliation numbers after each name (`Ann Lee1,2`) |
| `Contact Author` | Not stored |
| `Contact E-Mail` | Not stored |
| `Affiliation` | Affiliations, as a numbered list (`1 University A` on each line) that the author numbers point to. A single affiliation goes to every author |
| `Abstract` | Abstract |
| `Website` | A related resource of the poster |
| `LinkedIn`, `Instagram`, `Bluesky`, `X` | Not stored |
| `Comment` | Not stored |

You can add a file name column (`File name`) to link each row to its poster exactly.

Curious sheets usually don't name the poster files, so most rows are matched by title once the posters have been read.

## Limits

- File types: `.xlsx`, `.xls`, `.csv` or `.tsv`.
- Up to 10 MB in total, and up to 20,000 rows.
- An `.xls` file saved from a web page is not a real Excel file. Open it in Excel and save it as `.xlsx` or `.csv`.
