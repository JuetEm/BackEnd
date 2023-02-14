/** @format */

const header = document.querySelector('.p-navbar');

console.log(header);

window.addEventListener('scroll', function () {
  let value = window.scrollY;
  let bdl = header.classList;
  console.log(bdl);

  if (value > 1) {
    bdl.add('p-navbar_border');
  } else {
    bdl.remove('p-navbar_border');
  }
});
