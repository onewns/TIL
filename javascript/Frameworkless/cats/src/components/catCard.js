export default (cat) => {
  const catCard = document.createElement('div');
  const catImg = document.createElement('img');
  catImg.src = cat.url;
  catCard.className = 'cat-card';
  catCard.appendChild(catImg);
  return catCard
}