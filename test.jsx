const request = require("request");
const cheerio = require("cheerio");
const userAgentArray = require("user-agent-array");
const { exec } = require("child_process");

const fs = require("fs");
function randomSelectUserAgent() {
  return Math.floor(Math.random() * (899 - 0) + 0);
}

async function googleUrls(keyword, pages) {
  let urls = [];
  let searchUrl = `https://www.google.com/search?q=site:instagram.com+inurl:/p/+${keyword}&client=ubuntu-sn&biw=2486&bih=968&dpr=1&gl=in`;
  const proxyUrl = "http://username:password@ip:port";

  await fetchUrlsFromSearchPage(searchUrl, proxyUrl, urls);
  let currentPage = 2;
  while (currentPage < pages) {
    const nextPageUrl = getNextPageUrl(currentPage, keyword);
    if (!nextPageUrl) {
      console.log("no page available");
      break;
    }
    await fetchUrlsFromSearchPage(nextPageUrl, proxyUrl, urls);
    currentPage++;
  }
  urls = removeDuplicates(urls);
  console.log(`Fetched ${urls.length} URLs`);

  urls = urls.filter(function (el) {
    return el != null;
  });
  let newArr = [];
  for (let i = 0; i < urls.length; i++) {
    if (urls[i].includes("https://www.instagram.com/p/")) {
      let startParse = urls[i].indexOf("https://www.instagram.com/p/");
      currentPosturl = urls[i].slice(startParse, startParse + 40);
      newArr.push(currentPosturl);
    }
  }
  return newArr;
}

async function fetchUrlsFromSearchPage(url, proxyUrl, urls) {
  try {
    request.defaults({ proxy: proxyUrl });

    let randomSelectNumberUserAgent = randomSelectUserAgent();
    let userAgentRandom = userAgentArray[randomSelectNumberUserAgent];
    let options = {
      url,
      proxy: proxyUrl,
      mode: "cors",

      headers: {
        "cache-control": "no-cache",
        Connection: "keep-alive",

        "User-Agent": userAgentRandom,
      },
    };
    return new Promise((resolve, reject) => {
      request.get(options, (err, res, body) => {
        if (err) {
          console.log("Error", err);
          resolve();
        } else {
          const $ = cheerio.load(body);
          const linkElements = $("a");
          linkElements.each((i, el) => {
            let fetchedUrl = $(el).attr("href");
            console.log(fetchedUrl);
            urls.push(fetchedUrl);
          });
          resolve();
        }
      });
    });
  } catch (err) {
    fetchUrlsFromSearchPage(url, proxyUrl, urls);
    console.log("ERROR ACCURES DUE TO: ", err);
  }
}

function removeDuplicates(arr) {
  return arr.filter((item, index) => arr.indexOf(item) === index);
}

function getNextPageUrl(page, keyword) {
  let startIndex = Number((page - 1) * 10);
  return `https://www.google.com/search?q=site:instagram.com+inurl:/p/+${keyword}&start=${startIndex}&client=ubuntu-sn&biw=2486&bih=968&dpr=1&gl=in`;
}

module.exports = {
  googleUrls,
};
