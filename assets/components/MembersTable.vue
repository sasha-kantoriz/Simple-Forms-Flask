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
                        <th>Almarhum Suami/Istri</th>
                        <th>Nama lengkap Mertua perempuan</th>
                        <th>Almarhum Mertua perempuan</th>
                        <th>Nama lengkap Mertua laki-laki</th>
                        <th>Almarhum Mertua laki-laki</th>
                        <th>Alamat lengkap Mertua</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="member in members">
                        <td><router-link :to="{ name: 'user', params: { id: member.id } }">{{ member.full_name }}</router-link></td>
                        <td>{{ member.date_of_birth }}</td>
                        <td>{{ member.place_of_birth }}</td>
                        <td>{{ member.complete_address }}</td>
                        <td>{{ member.deceased }}</td>
                        <td>{{ member.spouse_full_name }}</td>
                        <td>{{ member.spouse_date_of_birth }}</td>
                        <td>{{ member.spouse_place_of_birth }}</td>
                        <td>{{ member.spouse_deceased }}</td>
                        <td>{{ member.mother_inlaws_full_name }}</td>
                        <td>{{ member.mother_inlaws_deceased }}</td>
                        <td>{{ member.father_inlaws_full_name }}</td>
                        <td>{{ member.father_inlaws_deceased }}</td>
                        <td>{{ member.father_inlaws_full_address }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        members: Array,
    }
}
</script>

<style>

</style>
