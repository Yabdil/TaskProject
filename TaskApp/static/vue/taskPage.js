const tasksData = [
                {description: "Premier element", is_completed:false},
                {description: "Premier element", is_completed:false}
]

var mainApp = new Vue({
    el: '#mainPage',
    delimiters: ["[[", "]]"],
    data: function () {
        return {
            tasks: tasksData,
            newItemDescription: '',
            name: "Abdillahi"
        }
    },
    methods: {
        addTask(){
            console.log("Clicked and added")
        },
        deleteTask(task){
            console.log("deleting the task", task)
        },
        completeTask(task){
            console.log("changing the state", task)
        }
    }
})


