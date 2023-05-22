const body = document.querySelector("body");
const pricetable = document.getElementById("pricetable");

// function for pulling prices data from api
const loadApiData = async () => {
  const url = "/api/europe";
  const response = await fetch(url);
  const data = await response.json();
  return data;
};

// inserting new dom elements (price information) into the table
const displayPrices = async () => {
  const url = "/api/europe";
  const response = await fetch(url);
  const data = await response.json();
  data.forEach((element) => {
    console.log("dodany element");
    pricetable.innerHTML += `<tr><td>${element.country}</td><td>${element.dieselprice}</td><td>${element.gasolineprice}</td><td>${element.lpgprice}</td></tr>`;
  });
};

displayPrices();
