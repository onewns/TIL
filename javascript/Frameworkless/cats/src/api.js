const BASE_URL = 'https://oivhcpn8r9.execute-api.ap-northeast-2.amazonaws.com/dev/api'

const parseResponse = async response => {
  const { status } = response;
  let data = null
  if (status === 200) {
    response = await response.json()
    data = response['data']
  } else if (status === 500) {
    alert('서버에 문제가 발생했습니다 다시 시도해주세요')
  } else if (status === 404) {
    alert('잘못된 요청입니다.')
  }
  return {
    status,
    data
  }
}

const request = async url => {
  const response = await fetch(url)
  return parseResponse(response)
}


const api = {
  async getRandomCats() {
    const response = await request(`${BASE_URL}/cats/random50`);
    if (response.status !== 200) {
      const response = await request(`${BASE_URL}/cats/random50`);
    }
    return response.data
  },
  async getCats(keyword) {
    const response = await request(`${BASE_URL}/cats/search?q=${keyword}`);
    return response.data
  },
  async getCatDetail(catId) {
    const response = await request(`${BASE_URL}/cats/${catId}`)
    return response.data
  }
}

export default api