
const { chromium } = require("playwright");

async function main() {
  const browser = await chromium.launch({
    headless: false,
  });

  const page = await browser.newPage();

  try {
    console.log("Membuka pencarian X...");

    await page.goto(
      "https://x.com/search?q=ubi%20bombing&src=typed_query&f=live",
      {
        waitUntil: "domcontentloaded",
        timeout: 60000,
      }
    );

    console.log("Halaman berhasil dibuka.");
    console.log("URL:", page.url());
    console.log("Silakan periksa browser yang terbuka.");
    console.log("Browser akan ditutup setelah 60 detik.");

    await page.waitForTimeout(60000);
  } catch (error) {
    console.error("Gagal membuka halaman:", error.message);
  } finally {
    await browser.close();
  }
}

main();
