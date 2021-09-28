# pdfgenerator

A Flask app in Docker that will generate PDF documents.

## Routes

### `/pdf?url={url}&filename={filename (optional)}`

Goal: Return a PDF document of the provided `url` with response of:

Content-Type: application/pdf
Content-Disposition: attachment; filename={filename}
