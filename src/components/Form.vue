<template>
  <div id="aida-container">
    <div id="aida" class="container">
      <div class="row">
        <div class="col-12">
          <form style="width:90%; margin:auto;">
            <div class="text-center">
              <h2
                style="padding: 20px;font-family: 'Lalezar', cursive;text-shadow: 1px 3px 0 #3F00FF;color : #884DCB"
              >ثبت نام کارگروه ها</h2>
            </div>

            <!-- <div style="display:table; font-family: 'PT Sans Narrow', sans-serif;font-size:20px"> -->
            <div class="form-group" style=" font-family: 'Lalezar', cursive;font-size:20px">
              <label for="nameInput" style="color:white">نام و نام خانوادگی</label>
              <input
                type="text"
                required="true"
                class="form-control"
                id="nameInput"
                style="direction: rtl"
                v-model="user.name"
                placeholder="نام و نام خانوادگی"
              />

              <!-- <small
              id="emailHelp"
              class="form-text text-muted"
              >We'll never share your email with anyone else.</small>-->
            </div>
            <!-- </div> -->
            <div class="mt-4 col-md-12"></div>
            <div class="form-group" style=" font-family: 'Lalezar', cursive;font-size:20px">
              <label for="emailInput" style="color:white">ایمیل</label>
              <input
                type="email"
                class="form-control"
                v-model="user.email"
                id="emailInput"
                placeholder="ایمیل"
              />
            </div>

            <div class="mt-4 col-md-12"></div>

            <div class="form-group" style=" font-family: 'Lalezar', cursive;font-size:20px">
              <label for="phoneNumberInput" style="color:white">شماره تماس</label>
              <input
                type="text"
                required="true"
                class="form-control"
                v-model="user.phone_number"
                id="phoneNumberInput"
                placeholder="شماره تماس"
              />
            </div>
            <div class="mt-4 col-md-12"></div>
            <div class="form-group" style=" font-family: 'Lalezar', cursive;font-size:20px">
              <label for="stdNumInput" style="color:white">شماره دانشجویی</label>
              <input
                type="text"
                class="form-control"
                v-model="user.student_number"
                id="stdNumInput"
                placeholder="شماره دانشجویی"
              />
            </div>

            <div class="mt-4 col-md-12" style="color: white;">
              <p>
                <span
                  class="form-group"
                  style=" color:white; font-family: 'Lalezar', cursive;font-size:20px"
                >تابستون شیراز هستی؟</span>
              </p>
              <table align="center" cellpadding="5px">
                <tr>
                  <th>
                    <label>
                      <input
                        v-model="user.in_shiraz"
                        :name="in_shiraz"
                        class="radio"
                        type="radio"
                        label="yes"
                        placeholder="جواب"
                        value="true"
                        padding="20px"
                      /> بله
                    </label>
                  </th>
                  <th>
                    <label>
                      <input
                        v-model="user.in_shiraz"
                        :name="in_shiraz"
                        class="radio"
                        type="radio"
                        label="no"
                        value="false"
                        placeholder="جواب"
                        padding="20px"
                      /> خیر
                    </label>
                  </th>
                </tr>
              </table>
            </div>

            <div class="mt-4 col-md-12" style="color: white">
              <p>
                <span
                  class="form-group"
                  style=" color:white; font-family: 'Lalezar', cursive;font-size:20px"
                >ترم تابستونه داری؟</span>
              </p>
              <table align="center" cellpadding="5px">
                <tr>
                  <th>
                    <label>
                      <input
                        v-model="user.term_tabestun"
                        :name="term_tabestun"
                        class="radio"
                        type="radio"
                        label="yes"
                        placeholder="جواب"
                        value="true"
                        padding="20px"
                      /> بله
                    </label>
                  </th>
                  <th>
                    <label>
                      <input
                        v-model="user.term_tabestun"
                        :name="term_tabestun"
                        class="radio"
                        type="radio"
                        label="no"
                        value="false"
                        placeholder="جواب"
                        padding="20px"
                      /> خیر
                    </label>
                  </th>
                </tr>
              </table>
            </div>

             <div class="mt-4 col-md-12" style="color: white;">
              <p>
                <span
                  class="form-group"
                  style=" color:white; font-family: 'Lalezar', cursive;font-size:20px"
                >ماشین داری؟</span>
              </p>
              <table align="center" cellpadding="5px">
                <tr>
                  <th>
                    <label>
                      <input
                        v-model="user.mashin"
                        :name="mashin"
                        class="radio"
                        type="radio"
                        label="yes"
                        placeholder="جواب"
                        value="true"
                        padding="20px"
                      /> بله
                    </label>
                  </th>
                  <th>
                    <label>
                      <input
                        v-model="user.mashin"
                        :name="mashin"
                        class="radio"
                        type="radio"
                        label="no"
                        value="false"
                        placeholder="جواب"
                        padding="20px"
                      /> خیر
                    </label>
                  </th>
                </tr>
              </table>
            </div>

            <div class="mt-4 col-md-12"></div>

            <div class="float-center" style="font-family: 'Lalezar', cursive; color: blue">
              <h2>گروه ها</h2>
            </div>

            <div class="mt-4 col-md-12"></div>

            <div
              class="form-group"
              v-bind:key="parent.pk"
              v-for="parent in parents"
              style=" font-family: 'Lalezar', cursive;;font-size:20px; color:white"
            >
              <label class="form-group-label" :for="'parent' + parent.pk">{{ parent.name }}</label>
              <input
                class="form-group-input"
                :id="'parent' + parent.pk"
                @change="parentCheckboxChanged"
                type="checkbox"
                :value="parent.pk"
              />
            </div>

            <div class="mt-4 col-md-12"></div>

            <div
              class="form-group"
              style=" font-family: 'Lalezar', cursive;font-size:20px;color:white"
            >
              <h2 style="color: blue">زیر گروه ها</h2>
            </div>

            <div class="mt-4 col-md-12"></div>

            <div
              class="form-group"
              v-bind:key="parent.pk"
              v-for="parent in chosenParents "
              style=" font-family: 'Lalezar', cursive;font-size:20px;color:white"
            >
              <div
                class="form-group"
                v-bind:key="category.pk"
                v-for="category in categories"
                v-if="category.parent.pk == Number(parent)"
              >
                <label class="form-group-label" :for="'category' + category.pk">
                  <span style="color:red">{{ category.parent.name }}</span>
                  {{ category.name }}
                </label>

                <input
                  class="form-group-input"
                  :id="'category' + category.pk"
                  @change="categoryCheckboxChanged"
                  type="checkbox"
                  :value="category.pk"
                />
              </div>
            </div>

            <div class="mt-4 col-md-12"></div>

            <div
              class="form-group"
              style=" font-family: 'Lalezar', cursive;font-size:20px;color:white"
            >
              <h2 style="color: blue">سوالات</h2>
            </div>

            <div class="mt-4 col-md-12"></div>

            <div
              class="form-group"
              style="font-family: 'Lalezar'"
              v-bind:key="category.pk"
              v-for="category in chosenCategories"
            >
              <div class="form-group" v-bind:key="question" v-for="question in questions">
                <div class="form-group" v-if="question.category.pk == category">
                  <div class="form-group" v-if="question.is_bool == false">
                    <p>
                      <span style="color:red">{{ question.category.name }} :</span>
                      {{ question.text }}
                    </p>
                    <input
                      v-model="info[question.pk]"
                      class="form-control"
                      type="text"
                      placeholder="جواب"
                    />
                    <div class="mt-4 col-md-12"></div>
                  </div>

                  <div
                    class="form-group"
                    v-else
                    style="font-family: 'Lalezar', cursive; display:inline-block"
                  >
                    <p>
                      <span style="color:red">{{ question.category.name }} :</span>
                      {{ question.text }}
                    </p>
                    <table align="center" cellpadding="5px">
                      <tr>
                        <th>
                          <label>
                            <input
                              v-model="info[question.pk]"
                              :name="question.pk"
                              class="radio"
                              type="radio"
                              label="yes"
                              placeholder="جواب"
                              value="true"
                              padding="20px"
                            /> بله
                          </label>
                        </th>
                        <th>
                          <label>
                            <input
                              v-model="info[question.pk]"
                              :name="question.pk"
                              class="radio"
                              type="radio"
                              label="no"
                              value="false"
                              placeholder="جواب"
                              padding="20px"
                            /> خیر
                          </label>
                        </th>
                      </tr>
                    </table>
                    <div v-if="info[question.pk] == 'true' ">
                      <div class="form-group">
                        <p>
                          <span style="color:red">:توضیح بده</span>
                          
                        </p>
                        <input
                          v-model="textt[question.pk]"
                          class="form-control"
                          type="text"
                          placeholder="جواب"
                        />
                        <div class="mt-4 col-md-12"></div>
                      </div>
                    </div>
                    <!-- <div v-else> {{ info[question.pk]['text'] = '' }} </div> -->
                  </div>
                </div>
              </div>
            </div>

            <div class="mt-4 col-md-12"></div>

            <p
              @click="doRegister"
              class="btn btn-outline-primary"
              style=" font-family: 'Lalezar', cursive; font-size:20px;color:white"
            >ثبت</p>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { constants } from 'crypto';
export default {
  name: "Form",
  data() {
    return {
      user: {
        name: null,
        email: "",
        phone_number: null,
        student_number: null,
        address: "",
        in_shiraz: null,
        term_tabestun: null,
        mashin: null
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
      textt: {},
      parentsMap: {},
      categoriesMap: {},
      questionsMap: {}
    };
  },
  methods: {
    async doRegister() {
      const vinst = this;

      // console.log(this.user);

      async function createuser(a) {
        // console.log('1');
        let response = await axios.post(
          "http://api.moarefe98.ir/signup/user/",
          a.user
        );

        // console.log('2');
        if (response.status == 200) {
          // console.log('success: ',response);
          var upk = response.data["pk"];
          // console.log(a.userpk);
        } else {
          console.log("error: ", response);
        }

        return upk;
      }

      this.userpk = await createuser(this);
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

      var answerlist = [];

      for (var item in this.info) {
        if (this.questionsMap[item].is_bool == true) {
          // console.log('tushe');
          // console.log(this.info);
          // console.log(item);
          // console.log(this.textt);
          // console.log(this.textt[item]);
          // console.log(this.info[item]);
          if (this.info[item] == 'true'){
            answerData = {
            user: this.userpk,
            question: item,
            text: this.textt[item],
            boolean: this.info[item]
          };
          } else {
            answerData = {
            user: this.userpk,
            question: item,
            text: "",
            boolean: this.info[item]
          };
          }
          
          // console.log(answerData);
          answerlist.push(answerData);
          // console.log(answerData);
        } else {
          // console.log('biruneshe');
          answerData = {
            user: this.userpk,
            question: item,
            text: this.info[item],
            boolean: null
          };
          answerlist.push(answerData);
          // console.log(answerData);
        }
      }
      // console.log(answerlist);
      var answerres = await axios.post(
        "http://api.moarefe98.ir/signup/answer/",
        answerlist
      );
      // console.log(answerres);

      answerlist = [];
      this.info = [];
      this.chosenQuestions = [];
      this.chosenCategories = [];
      this.chosenParents = [];
      alert('با تشکر. فرم شما ثبت شد.');
      window.location.replace("http://moarefe98.ir");
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
    axios.get("http://api.moarefe98.ir/signup/parent").then(response => {
      // console.log(response.data);
      this.parents = response.data;
      for (let item of this.parents) {
        this.parentsMap[item.pk] = item;
      }
    }),
      axios.get("http://api.moarefe98.ir/signup/category").then(response => {
        // console.log(response.data);
        this.categories = response.data;
        for (let item of this.categories) {
          this.categoriesMap[item.pk] = item;
        }
      }),
      axios.get("http://api.moarefe98.ir/signup/question").then(response => {
        // console.log(response.data);
        this.questions = response.data;
        for (let item of this.questions) {
          this.questionsMap[item.pk] = item;
        }
      });
  }
};
</script>


<style scoped>
#aida-container {
  /* background-color: red; */
  width: 100%;
}
#aida {
  /* background-color: #212121; */
  background-color: transparent;
  border: 4px solid #4b0082;
  border-radius: 18px;
  vertical-align: middle;
  margin: 30px auto 0 auto;
  width: 27%;
  min-width: 320px;
}

.form-group,
.form-control {
  width: 90%;
  margin: auto;
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