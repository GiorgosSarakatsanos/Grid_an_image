const express = require('express');
const multer = require('multer');
const PDFDocument = require('pdfkit');
const fs = require('fs');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(express.static('public')); // Serve static files from 'public' directory

app.post('/upload', upload.array('images'), (req, res) => {
    console.log(`Received ${req.files.length} images for paper size ${req.body.paper_size}`);
    // Here, you could process the images or store them as needed.
    res.send('Images uploaded successfully');
});

app.get('/generate-pdf', (req, res) => {
    const doc = new PDFDocument();
    let buffers = [];
    doc.on('data', buffers.push.bind(buffers));
    doc.on('end', () => {
        let pdfData = Buffer.concat(buffers);
        res.writeHead(200, {
            'Content-Length': Buffer.byteLength(pdfData),
            'Content-Type': 'application/pdf',
            'Content-Disposition': 'attachment; filename=generatedPdf.pdf',
        }).end(pdfData);
    });

    // Example PDF content
    doc.fontSize(25).text('PDF Generation Example', 100, 100);
    // Add more content as needed
    doc.end();
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});