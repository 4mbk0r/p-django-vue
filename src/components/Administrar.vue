<template>
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>LiSTA</h2>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

const Cookies = require('js-cookie');
export default {
    data() {
        return {
            fields: [
                { key: 'titulo', label: 'Titulo' },
                { key: 'nombre', label: 'Nombre' },
                { key: 'action', label: 'Acccion' },
            ],
            books: [],
            dato: '',
        }
    },
    methods: {
        getBooks() {
            const path = process.env.API_URL + "/api/v1.0/books/"
            axios.get(path).then((response) => {
                this.books = response.data
            })
                .catch((error) => {
                    console.log(error);
                })
        },
        editar(data) {
            console.log(data)
        },
        adicionar() {
            const path = process.env.API_URL + "/adicionar/"
            axios.post(path, {
                name: 'name',
                date: 'date'
            }).then((response) => {
                console.log(response.data);
            })
        },
        close() {
            const path = process.env.API_URL + "/logout/"
            console.log(path)
            //this.user.token=null
            console.log(JSON.parse(localStorage.getItem('user')))
            var datos = {
                token: localStorage.getItem('token'),
                name: JSON.parse(localStorage.getItem('user')).username,
                nuevo: '',
            }
            axios({
                method: "post",
                url: path,
                data: datos,
                headers: {
                    'Content-Type': 'application/json',
                    "X-CSRFToken": Cookies.get('csrftoken')
                },

            }).then((response) => {
                console.log(response.data)
                if (response.status == 200) {
                    console.log(response)
                    localStorage.clear()
                    localStorage.removeItem('token-user')
                    localStorage.removeItem('data-user')
                    alert('se cerrado session')

                    this.$router.push('/')

                }
            })
                .catch((error) => {
                    console.log(error);
                })
        }
    },
    created() {
        this.getBooks()
    }

}
</script>
