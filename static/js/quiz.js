// quiz_script.js

var app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data() {
      return {
        category: "{{category}}",
        questions: []
      };
    },
    methods: {
      getQuestions() {
        var _this = this;
        fetch(`/tests/get_quiz/?category=${_this.category}`)
          .then(response => response.json())
          .then(result => {
            console.log(result);
            _this.questions = result.data.map(question => {
              return { ...question, correct: null };
            });
          });
      },
      checkAnswer(event, uid) {
        // Nothing to do here, remove this method if not needed
      },
      checkAnswers() {
        this.questions.forEach(question => {
          let answeredCorrectly = false;
          question.answers.forEach(answer => {
            const inputElement = document.getElementById(question.uid + answer.answer);
            if (inputElement.checked) {
              if (answer.is_correct) {
                console.log("Your answer is correct");
                question.correct = true;
                answeredCorrectly = true;
              } else {
                console.log("Your answer is incorrect");
                question.correct = false;
              }
            }
          });
          if (!answeredCorrectly) {
            question.correct = false;
          }
        });
      }
    },
    created() {
      this.getQuestions();
    }
  });
  