function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


var app = new Vue({
    el: '#mainBody',
    delimiters: ["[[", "]]"],
    data: function () {
        return {
            errorMessage: 'Le mot de passe ou email est invalide',
            email: '',
            password: '',
            isError: false
        }
    },
    methods: {
    onSubmit(){
        console.log("clicked")
       this.authenticateUser()
    },

    async authenticateUser(){
      try {
      const configs = {
        headers: {
            "X-CSRFToken": csrftoken
        }
      }
        const response = await axios.post('login',{email: 'test3@gmail.com',
                               password: '123456789'},configs);
        console.log(response);
      } catch (error) {
        console.error(error);
      }
    }

    }
})


