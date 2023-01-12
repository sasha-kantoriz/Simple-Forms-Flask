<template>
  <FormComponent/>

  <UsersTable v-if="loggedIn" :users="usersData"/>

</template>

<script>
import FormComponent from './components/FormComponent.vue'
import UsersTable from './components/UsersTable.vue'

export default {
  name: 'App',
  components: {
    FormComponent,
    UsersTable
  },
  data() {
    return {
        loggedIn: authorized,
        usersData: users
    }
  },
}
</script>

<style scoped>

</style>
