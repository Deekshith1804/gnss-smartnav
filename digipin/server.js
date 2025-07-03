const app = require('./src/app');
const PORT = process.env.PORT || 10000;

app.listen(PORT, '0.0.0.0', () => {
  console.log(`DIGIPIN API is running and API docs can be found at http://localhost:${PORT}/api-docs`);
});
