import header from './components/header.js'
import searchBar from './components/searchBar.js';
import banner from './components/banner.js';
import searchResult from './components/searchResult.js';
import catDetail from './components/catDetail.js';

import registry from './registry.js';

import api from './api.js'

registry.add('header', header);
registry.add('searchBar', searchBar);
registry.add('banner', banner);
registry.add('searchResult', searchResult);
registry.add('catDetail', catDetail);

const state = {
  resultLoading: false,
  bannerLoading: false,
  detailLoading: false,
  catDetailVisible: false,
  cats: null,
  keywords: [],
  randomCats: null,
  cat: null
}

const render = (state) => {
    const main = document.querySelector('.main');
    const newMain = registry.renderRoot(main, state, events);
    main.replaceWith(newMain);
}

const events = {
  async toggleLoading (section) {
    state[section] = !state[section];
    render(state);
  },
  async getRandomCats () {
    this.toggleLoading('bannerLoading');
    let rcats = await api.getRandomCats();
    if (!rcats) {
      return
    }
    state.randomCats = [...rcats];
    this.toggleLoading('bannerLoading');
  },
  async getCats (keyword) {
    this.toggleLoading('resultLoading');
    state.cats = await api.getCats(keyword);
    if (!state.keywords.find(prekey => prekey === keyword)) {
      state.keywords.push(keyword);
      if (state.keywords.length > 5) {
        state.keywords.shift();
      }
    }
    this.toggleLoading('resultLoading');
  },
  async getCatDetail(catId) {
    state.catDetailVisible = true;
    this.toggleLoading('detailLoading');
    state.cat = await api.getCatDetail(catId);
    this.toggleLoading('detailLoading');
  },
  closeCatDetail() {
    state.catDetailVisible = false;
    state.cat = null;
    render(state);
  },
  closeCatDetailEsc(keyevent) {
    console.log(1)
    if (keyevent.key === 'Escape') {
      state.catDetailVisible = false;
      state.cat = null;
      render(state);
    }
  },
}

if (!state.randomCats) {
  events.getRandomCats()
}


export default () => {
  render(state)
}