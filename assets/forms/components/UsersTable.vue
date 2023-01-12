<template>
    <div id="table" class="table-container">
        <div class="table-wrapper">
            <div class="table-header">
                <h3>All users <a href="/#table">#</a></h3>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>
                            Name
                            <div class="sorting" @click="sorting('name')">
                                <img src="../resources/up.png"/>
                                <img src="../resources/down.png"/>
                            </div>
                        </th>
                        <th>
                            Phone
                            <div class="sorting" @click="sorting('phone')">
                                <img src="../resources/up.png"/>
                                <img src="../resources/down.png"/>
                            </div>
                        </th>
                        <th>
                            Email
                            <div class="sorting" @click="sorting('email')">
                                <img src="../resources/up.png"/>
                                <img src="../resources/down.png"/>
                            </div>
                        </th>
                        <th>Link</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(user, index) in sortedUsers" :key="index">
                        <td><a :href="`/user/${user.id}`">{{ user.name }}</a></td>
                        <td>{{ user.phone }}</td>
                        <td>{{ user.email }}</td>
                        <td><a class="btn btn-primary" type="button" v-if="user.children.length > 0" :href="`/children/${user.id}`">Children</a></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        users: Array
    },
    data() {
        return {
            sortOrdering: true,
            sortField: 'name',
            usersData: users,
        }
    },
    methods: {
        sorting(key) {
            if (key === this.sortField) {
                this.sortOrdering = !this.sortOrdering;
            }
            this.sortField = key;
        }
    },
    computed: {
        sortedUsers() {
            return this.usersData.sort((a,b) => {
                return this.sortOrdering ? a[this.sortField] > b[this.sortField] : a[this.sortField] < b[this.sortField]
            });
        }
    }
}
</script>
<style scoped>
.sorting {
    display: inline;
}
img {height: 17px;}
</style>