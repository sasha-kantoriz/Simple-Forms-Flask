<template>
    <div class="table-container" id="table">
        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th>Nama Lengkap</th>
                        <th>Tanggal Lahir</th>
                        <th>Tempat Lahir</th>
                        <th>Alamat Lengkap</th>
                        <th>Almarhum</th>
                        <th>Nama lengkap Suami/Istri</th>
                        <th>Tanggal Lahir Suami/Istri</th>
                        <th>Tempat Lahir Suami/Istri</th>
                        <th>Nama lengkap Mertua</th>
                        <th>Alamat lengkap Mertua</th>
                        <th>Almarhum Mertua</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="member in members">
                        <td>{{ member.full_name }}</td>
                        <td>{{ member.date_of_birth }}</td>
                        <td>{{ member.place_of_birth }}</td>
                        <td>{{ member.complete_address }}</td>
                        <td>{{ member.deceased }}</td>
                        <td>{{ member.spouse_full_name }}</td>
                        <td>{{ member.spouse_date_of_birth }}</td>
                        <td>{{ member.spouse_place_of_birth }}</td>
                        <td>{{ member.inlaws_full_name }}</td>
                        <td>{{ member.father_inlaws_full_address }}</td>
                        <td>{{ member.father_inlaws_deceased }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
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
