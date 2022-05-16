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
    }

    }
})

console.log("haha vue is charged")
