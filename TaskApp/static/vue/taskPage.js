var mainApp = new Vue({
    el: '#mainPage',
    delimiters: ["[[", "]]"],
    data: function () {
        return {
            tasks: '' ,
            newItemDescription: '',
            isCompletedActivated: false,
            myOwnTasks: false,
            idOfUser: 3

        }
    },
    methods: {
        async getTasks(){
          try {
            const response = await axios.get('getTasks')
            this.tasks = JSON.parse(response.data)
          } catch (error) {
            console.error(error);
          }
        },
        async addTask(){
          try {
             const data = {description:this.newItemDescription, created_by: this.idOfUser}
             const response = await axios.post('addTask',data)
             this.newItemDescription = ''
             this.getTasks()
          } catch(error) {
             console.log(error)
          }
        },
        async deleteTask(id){
          try {
            const url = `deleteTask/${id}`
            const response = await axios.delete(url)
            this.getTasks()
          } catch(error){
            console.log(error)
          }
        },
        async completeTask(id){
          try {
            const url = `completeTask/${id}`
            const response = await axios.put(url, {"is_completed":true})
            this.getTasks()
          } catch(error){
            console.log(error)
          }
        },
        filterCompletedTasks(){
            this.isCompletedActivated = !this.isCompletedActivated
            if (!this.isCompletedActivated){ // If the filter is not activated, we fetch from the server
                this.getTasks()
            }
            const filteredTasks = this.tasks.filter(task => Boolean(task.fields.is_completed))
            this.tasks = filteredTasks
        },
        filterOwnTasks(){
            this.myOwnTasks = !this.myOwnTasks
            if (!this.myOwnTasks){ // If the filter is not activated, we fetch again from the server
                this.getTasks()
            }
            const filteredTasks = this.tasks.filter(task => task.fields.created_by === this.idOfUser)
            this.tasks = filteredTasks
        },
       async clearAllTasks(){
        try {
            const url = `clearAllTasks`
            const response = await axios.delete(url)
          } catch(error){
            console.log(error)
          }
        }

    },
    created(){
      this.getTasks()
    }
})


