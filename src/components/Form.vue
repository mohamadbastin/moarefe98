<template id="aida">
  <div id="aida" class="container">
    <div class="row">
      <div class="col-12">
        <form>
          <div class="text-center">
            <h2 style="padding: 20px">Moarefe Registration</h2>
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input
              type="email"
              class="form-control"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              v-model="user.email"
              placeholder="Enter email"
            />
            <small
              id="emailHelp"
              class="form-text text-muted"
            >We'll never share your email with anyone else.</small>
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">First Name</label>
            <input
              type="password"
              class="form-control"
              v-model="user.first_name"
              id="exampleInputPassword1"
              placeholder="Password"
            />
          </div>
          <div class="text-left">check here bitch</div>
          <div></div>

          <div class="form-check">
            <input type="checkbox" class="form-check-input" id="exampleCheck1" />
            <label class="form-check-label" for="exampleCheck1">Check me out</label>
          </div>
          <div></div>
          <div class="form-group">
            <label for="exampleFormControlSelect1">Example select</label>
            <select class="form-control" id="exampleFormControlSelect1">
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select>
          </div>

          <div class="form-check" v-bind:key="parent.pk" v-for="parent in parents">
            <input
              class="form-check-input"
              :id="'parent' + parent.pk"
              @change="parentCheckboxChanged"
              type="checkbox"
              :value="parent.pk"
            />
            <label class="form-check-label" :for="'parent' + parent.pk">{{ parent.name }}</label>
          </div>

          <div class="form-check">
            <h2>categories</h2>
          </div>

          <div class="form-check" v-bind:key="parent.pk" v-for="parent in chosenParents">
            <div
              class="form-check"
              v-bind:key="category.pk"
              v-for="category in categories"
              v-if="category.parent == Number(parent)"
              
            >
              <input
                class="form-check-input"
                :id="'category' + category.pk"
                @change="categoryCheckboxChanged"
                type="checkbox"
                :value="category.pk"
              />
              <label class="form-check-label" :for="'category' + category.pk">{{ category.name }}</label>
            </div>
          </div>

          <div class="form-check">
            <h2>Questions</h2>
          </div>

          <div class="form-check" v-bind:key="category.pk" v-for="category in chosenCategories">
            <div class="form-check" v-bind:key="question" v-for="question in questions">
              <div class="form-check" v-if="question.category == category">
                <div class="form-check" v-if="question.is_bool == false">
                    <p> {{ question.text }} </p>
                    <input
                    
                      class="form-control"
                      type="text"
                      placeholder="answer"
                      > 
                </div>
                <div class="form-check" v-else>
                  <p> {{ question.text }} </p>
                  <label><input
                      name="boz"
                      class="radio"
                      type="radio"
                      label="yes"
                      placeholder="answer"
                      padding="20px"
                      > yes </label>
                      <div></div>
                      <label><input
                      name="boz"
                      class="radio"
                      type="radio"
                      label="yes"
                      placeholder="answer"
                      padding="20px"
                      > no </label>

                </div>
              </div>
            </div>
          </div>

          <p @click="doRegister" class="btn btn-primary">Submit</p>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Form",
  data() {
    return {
      user: {
        first_name: "",
        last_name: "aefawe",
        email: "",
        phone_number: "14312",
        student_number: null
      },
      parents: [],
      chosenParents: [],
      categories: [],
      chosenCategories: [],
      questions: [],
      chosenQuestions: [],
      dataObject: {}
    };
  },
  methods: {
    doRegister() {
      // const vinst = this;
      axios
        .post("http://localhost:8000/signup/user/", this.user)
        .then(response => {
          console.log(response);
        })
        .catch(err => {
          console.log(err);
        });
    },
    parentCheckboxChanged($event) {
      if ($event.target.checked) {
        this.chosenParents.push($event.target.value);
        console.log(this.chosenParents);
      } else {
        let index = this.chosenParents.indexOf($event.target.value);
        if (index > -1) {
          this.chosenParents.splice(index, 1);
        }
      }
    },
    categoryCheckboxChanged($event) {
      if ($event.target.checked) {
        this.chosenCategories.push($event.target.value);
        console.log(this.chosenCategories);
      } else {
        let index = this.chosenCategories.indexOf($event.target.value);
        if (index > -1) {
          this.chosenCategories.splice(index, 1);
        }
      }
    }
  },
  mounted() {
    axios.get("http://localhost:8000/signup/parent").then(response => {
      console.log(response.data);
      this.parents = response.data;
    }),
      axios.get("http://localhost:8000/signup/category").then(response => {
        console.log(response.data);
        this.categories = response.data;
      }),
      axios.get("http://localhost:8000/signup/question").then(response => {
        console.log(response.data);
        this.questions = response.data;
      });
  }
};
</script>


<style scoped>
#aida {
  background: #e3e3e3;
}
</style>








// <div class="form-check" v-bind:key="category.pk" v-for="category in chosenCategories">
//             <div
//               class="form-check"
//               v-bind:key="question.pk"
//               v-if="question.category == Number(category)"
              

//               v-for="question in questions"
//             >
//               <input
//                 class="form-check-input"
//                 :id="'question' + question.pk"
//                 type="checkbox"
//                 :value="question.pk"
//               />
//               <!-- TODO -->
//               <label class="form-check-label" :for="'question' + question.pk"> {{ question.text }}</label>
//             </div>
//           </div>