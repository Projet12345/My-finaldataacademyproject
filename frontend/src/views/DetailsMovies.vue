<template>
  <v-container class="movie-details">
    <v-row>
      <v-col>
        <v-card>
          <v-container v-if="movieDetails!=null" fluid>
            <v-row>
              <v-col cols="12">
                <v-card flat>
                  <v-row>
                    <v-col cols="12" md="3">
                      <v-img
                        :src="getImageUrl(movieDetails.poster_path)"
                        aspect-ratio="0.9"
                        class="rounded-lg"
                      ></v-img>
                    </v-col>
                    <v-col cols="12" md="9">
                      <v-card-title class="text-h5 font-weight-bold mb-2">{{
                        movieDetails.title
                      }}</v-card-title>
                      <v-card-subtitle
                        class="text-subtitle-1 font-weight-medium mb-4"
                        >{{ movieDetails.release_date }}</v-card-subtitle
                      >
                      <v-card-text class="text-body-1">
                        <p>{{ movieDetails.overview }}</p>
                        <v-divider class="my-2"></v-divider>
                        <div class="d-flex align-center mb-2">
                          <v-icon color="warning" small class="mr-1"
                            >mdi-star</v-icon
                          >
                          <span class="font-weight-medium">{{
                            movieDetails.vote_average
                          }}</span>
                          <span class="text-grey-darken-1 ml-1"
                            >({{ movieDetails.vote_count }} votes)</span
                          >
                        </div>
                        <div class="d-flex align-center mb-2">
                          <v-icon color="grey-darken-1" small class="mr-1"
                            >mdi-chart-line</v-icon
                          >
                          <span class="font-weight-medium">{{
                            movieDetails.popularity
                          }}</span>
                        </div>
                      </v-card-text>
                    </v-col>
                  </v-row>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-card flat tile>
                  <v-card v-if="authToken!=null" flat tile>
                    <v-card-title>Add a Comment</v-card-title>
                  <v-card-text >
                    <v-form v-model="valid" @submit.prevent="addComment" ref="commentForm">
                      <v-text-field
                        label="Name"
                        v-model="newComment.author"
                        :rules="[rules.required]"
                        required
                      ></v-text-field>
                      <v-textarea
                        label="Comment"
                        v-model="newComment.content"
                        :rules="[rules.required]"
                        required
                      ></v-textarea>
                      <v-btn :disabled="!valid" type="submit" color="primary">Submit</v-btn>
                    </v-form>
                  </v-card-text>
                  </v-card>
                  <v-card flat tile>
                    <v-card-title>Comments</v-card-title>
                    <v-card-text>
                      <v-card
                        flat
                        v-for="comment in comments"
                        :key="comment.id"
                        class="mb-4 border border-lg"
                        :class="{
                          'border-success': comment.review == true,
                          'border-error': comment.review ==false,
                        }"
                      >
                        <v-card-title class="d-flex justify-space-between">
                          {{ comment.user.email }}

                          <span
                            :class="{
                              'text-success': comment.review == true,
                              'text-error': comment.review ==false,
                            }"
                            class="font-weight-medium ml-2"
                          >
                            <v-icon
                              :color="comment.review == true ? 'success' : 'error'"
                              small
                              class="ml-2"
                            >
                              {{
                                comment.review == true
                                  ? "mdi-emoticon-happy"
                                  : "mdi-emoticon-sad"
                              }}
                            </v-icon>
                            {{
                              comment.review == true ? "Positif Review" : "Negatif Review"
                            }}
                          </span>
                        </v-card-title>
                        <v-card-text>{{ comment.content }}</v-card-text>
                        <v-card-subtitle>{{
                          comment.created_at
                        }}</v-card-subtitle>
                      </v-card>
                    </v-card-text>
                  </v-card>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, reactive,computed, onMounted} from "vue";
import { useStore } from 'vuex'
import axios from 'axios';
// Accéder au store
const store = useStore()

const authToken =  computed(() => store.state.moviesstore.authToken)
const userAuth = computed(() => store.state.moviesstore.user)
const valid = ref(false);
const props = defineProps({
  movieId: {
    type: Number,
    required: true,
  },
  id: {
      type: Number,
      required: true,
    },
},
);


 onMounted(() => {
  window.scrollTo(0,0)
  loadMovie()
  fetchComments()
 });
const movieDetails = computed(() => store.state.moviesstore.currentMovie)

  const  loadMovie= (async () => {

  await store.dispatch('moviesstore/fetchMovieById',props.id);
});


const getImageUrl = (path) => {
    return `https://image.tmdb.org/t/p/w185${path}`
  }
const comments = ref([]);

const newComment = reactive({
  author: "",
  content: "",
});

const rules = {
  required: (value) => !!value || "Ce champ est requis.",
  
};

// add comment
const addComment = () => {
  if (valid.value) {
    const newCommentObj = {
      user_name: newComment.author,
      user: 1,
      film_id: props.id, 
      content: newComment.content,
      review: false, 
    };

    axios.post('http://localhost:8000/api/comment/', newCommentObj)
      .then((response) => {
        comments.value.push(response.data);
        newComment.author = "";
        newComment.content = "";
      })
      .catch((error) => {
        console.error('Erreur lors de l\'ajout du commentaire:', error);
      });
  }
};
// get comment by film_id
  const fetchComments = () => {
  axios.get('http://127.0.0.1:8000/api/comment/', {
      params: {
          film_id: props.id
      }
  })
  .then((response) => {
      comments.value = response.data; 
  })
  .catch((error) => {
      console.error('Error during fetching data :', error);
  });
};
</script>

<style>
.movie-details {
  padding: 2rem;
}
</style>