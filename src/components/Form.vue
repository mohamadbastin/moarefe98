<template id="aida">
<div class="float-center">
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
              :value= "parent.pk"
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
              v-if="category.parent.pk == Number(parent)"
              
            >
              <input
                class="form-check-input"
                :id="'category' + category.pk"
                @change="categoryCheckboxChanged"
                type="checkbox"
                :value="category.pk"
              />
              <label class="form-check-label" :for="'category' + category.pk"> {{ category.parent.name }} {{ category.name }}</label>
            </div>
          </div>

          <div class="form-check">
            <h2>Questions</h2>
          </div>

          <div class="form-check" v-bind:key="category.pk" v-for="category in chosenCategories">
            <div class="form-check" v-bind:key="question" v-for="question in questions">
              <div class="form-check" v-if="question.category.pk == category">
                <div class="form-check" v-if="question.is_bool == false">
                    <p> {{ question.category.name }} {{ question.text }} </p>
                    <input
                      v-model="info[question.pk]"
                      class="form-control"
                      type="text"
                      placeholder="answer"
                      > 
                </div>
                <div class="form-check" v-else>
                  <p> {{ question.category.name }} {{ question.text }} </p>
                  <label><input
                      v-model="info[question.pk]"
                      :name="question.pk"
                      class="radio"
                      type="radio"
                      label="yes"
                      placeholder="answer"
                      value= true
                      padding="20px"
                      > yes </label>
                      <div></div>
                      <label><input
                      v-model="info[question.pk]"
                      :name="question.pk"
                      class="radio"
                      type="radio"
                      label="no"
                      value= false
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
      userpk: null,
      parents: [],
      chosenParents: [],
      categories: [],
      chosenCategories: [],
      questions: [],
      chosenQuestions: [],
      dataObject: {},
      info: {},
      parentsMap : {},
      categoriesMap : {},
      questionsMap: {}
    };
  },
  methods: {
    async doRegister() {
      const vinst = this;
      
      // console.log(this.user);

      async function createuser(a) { 
        // console.log('1');
        let response = await axios.post("http://localhost:8000/signup/user/", a.user)
        
        // console.log('2');
        if (response.status == 200) {
          // console.log('success: ',response);
          var upk = response.data["pk"];
          // console.log(a.userpk);
        } else {
          console.log('error: ',response);
        }

        return upk;
      
        }

        this.userpk = await createuser(this)
        // .then((res)=>{
        //     // console.log(res);
        //     this.userpk = res;
            // console.log(this.userpk);
            // console.log(this.userpk);
        // });
        // console.log("info:");
        // console.log(this.info);
        // console.log(this.userpk);
        
        var answerData = {};

        var answerlist=[];


        for (var item in this.info) {
            if (this.questionsMap[item].is_bool == true) {
              // console.log('tushe');
              answerData = {
                "user": this.userpk,
                "question": item,
                "text": "",
                "boolean": this.info[item]
              }
              answerlist.push(answerData);
              // console.log(answerData);
            } else {
              // console.log('biruneshe');
              answerData = {
                "user": this.userpk,
                "question": item,
                "text": this.info[item],
                "boolean": null,
              }
              answerlist.push(answerData);
              // console.log(answerData);
            }
        }
        console.log(answerlist);
        var answerres= await axios.post('http://localhost:8000/signup/answer/', answerlist);
        console.log(answerres);

        answerlist = [];
        this.info = [];
        this.chosenQuestions=[];
        this.chosenCategories = [];
        this.chosenParents=[];
        
    },
    parentCheckboxChanged($event) {
      // console.log(this.parentsMap[$event.target.value])
      if ($event.target.checked) {
        // console.log($event.target.value)
        this.chosenParents.push($event.target.value);
        
        // console.log(this.chosenParents);
      } else {
        let index = this.chosenParents.indexOf($event.target.value);
        if (index > -1) {
          this.chosenParents.splice(index, 1);
        }
          let temp = this.chosenCategories.slice(0);
          // console.log('set');
          // console.log('temp:',temp);
          // console.log('cC:', this.chosenCategories);
          for (var cat in temp) {
            // console.log('cC list:', this.chosenCategories);
            // console.log('temp list :', temp);
            // console.log('temp[cat]: ',temp[cat]);
            // console.log('temp[cat] obj: ',this.categoriesMap[temp[cat]]);
            // console.log('cC[cat]: ', this.chosenCategories[cat]);
            // console.log('cC[cat] obj: ', this.categoriesMap[this.chosenCategories[cat]]);
            // console.log(this.categoriesMap[temp[cat]].parent.pk == $event.target.value);
            //   console.log(this.categoriesMap[this.chosenCategories[cat]].parent.pk == $event.target.value);
              // console.log('catlist:');
              // console.log('cC: ',this.categoriesMap[this.chosenCategories[temp[cat]]]);
              // console.log('cat:');
              // console.log(this.chosenCategories[cat]);
              // console.log('value:');
              // console.log($event.target.value);
              
            if (this.categoriesMap[temp[cat]].parent.pk == $event.target.value) {
              // console.log('sag in if');
              // console.log('value: ',$event.target.value);
              var indexx = this.chosenCategories.indexOf(temp[cat]);
              // console.log('index: ',indexx);
              if (indexx > -1) {
                this.chosenCategories.splice(indexx, 1);
          //       // console.log(this.chosenCategories);
              }
          }
      }
      temp = [];
    }
    
    

  },
  categoryCheckboxChanged($event) {
      if ($event.target.checked) {
        this.chosenCategories.push($event.target.value);
        // console.log(this.chosenCategories);
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
      // console.log(response.data);
      this.parents = response.data;
      for(let item of this.parents){
        this.parentsMap[item.pk] = item;
      }
      
    }),
      axios.get("http://localhost:8000/signup/category").then(response => {
        // console.log(response.data);
        this.categories = response.data;
        for(let item of this.categories){
        this.categoriesMap[item.pk] = item;
      }
      }),
      axios.get("http://localhost:8000/signup/question").then(response => {
        // console.log(response.data);
        this.questions = response.data;
        for(let item of this.questions){
        this.questionsMap[item.pk] = item;}
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