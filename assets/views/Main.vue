<template>
    <MemberForm/>
    <MembersTable :members="members"/>
</template>

<script>
import axios from 'axios';

import MemberForm from '../components/MemberForm.vue';
import MembersTable from '../components/MembersTable.vue';


export default {
    components: {
        MemberForm,
        MembersTable,
    },
    data() {
        return {
            members: [],
        }
    },
    mounted() {
        axios.get('/members').then((response) => {
            this.members = response.data.members;
        });
    }
}
</script>

<style>

</style>