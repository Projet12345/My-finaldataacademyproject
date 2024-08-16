import axios from 'axios'

export default {
  namespaced: true,
  state: {
    authToken: null,
    user: null,
    status: null,
    loading: false,
    movies: [],
    currentPage: 1,
    totalPages: 0,
    currentMovie: null,
    token:"eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNTA2MDk5Y2VlZjUyZWVjZjEyODgzMTE3MDcyY2M3YyIsIm5iZiI6MTcyMzExNTQzNi4wNDQ1MSwic3ViIjoiNjE3ZTdiNmRjYmEzNmYwMDQzZTY1NDNkIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.47k7N8tvLEyz2VHo7LySsp15zT8ucZfOJ8x_6tLf0PU"
  },
  mutations: {
    SET_AUTH_TOKEN(state, token) {
      state.authToken = token
    },
    SET_USER(state, user) {
      state.user = user
    },
    SET_STATUS(state, status) {
      state.status = status
    },
    
    SET_MOVIES(state, movies) {
      state.movies = movies
    },
    SET_CURRENT_PAGE(state, page) {
      state.currentPage = page
    },
    SET_TOTAL_PAGES(state, totalPages) {
      state.totalPages = totalPages
    },
    SET_CURRENT_MOVIE(state, movie) {
      state.currentMovie = movie
    },
    SET_LOADING(state, loading) {
      state.loading = loading
    }
  },
  actions: {
    async login({ commit }, { email, password }) {
      commit('SET_LOADING', true)
      return axios.post('http://127.0.0.1:8000/api/auth/login/', { email, password })
        .then(response => {
          commit('SET_AUTH_TOKEN', response.data.access)
          commit('SET_STATUS', response.data.status)
          commit('SET_USER', response.data.user)
        })
        .catch(error => {
          console.error(error)
          throw error
        })
        .finally(() => {
          commit('SET_LOADING', false)
        })
    },
    async fetchTopRatedMovies({ commit, state }, page=1) {
      try {
        const response = await axios.get('http://localhost:8000/api/movies-list/', {
          
        })

        commit('SET_MOVIES', response.data.results)
        commit('SET_CURRENT_PAGE', response.data.page)
        commit('SET_TOTAL_PAGES', response.data.total_pages)
        console.log('2001')
      } catch (error) {
        console.error('Error fetching top rated movies:', error)
      }
    },
    async fetchMovieById({ commit,state }, movieId) {
      try {
        const response = await axios.get(`http://localhost:8000/api/movies/${movieId}/`, {
         
        })
        commit('SET_CURRENT_MOVIE', response.data)
        console.log(response.data)
      } catch (error) {
        console.error('Error fetching movie by ID:', error)
      }
    }
  
  }
}