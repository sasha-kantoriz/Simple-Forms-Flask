<template>
    <div class="form-container">
        <div class="form-wrapper">
            <form @submit.prevent="postNewMember">
                <div class="form-row">
                    <label for="role">Peran:</label>
                    <select id="role" class="form-select" v-model="formData.role">
                        <option v-for="opt in generations" :key="opt" :value="opt.value">{{ opt.title }}</option>
                    </select>
                </div>
                <div class="form-row form-row-inline">
                    <label for="gender">Jenis Kelamin:</label>
                    <div class="radio-inputs">
                        <div id="gender" class="form-check">
                            <label class="form-check-label" for="gender-1">Perempuan</label>
                            <input class="form-check-input" v-model="formData.gender" id="gender-1" name="gender" type="radio" value="female">
                        </div>
                        <div id="gender" class="form-check">
                            <label class="form-check-label" for="gender-2">Pria</label>
                            <input class="form-check-input" v-model="formData.gender" id="gender-2" name="gender" type="radio" value="male" checked>
                        </div>
                    </div>
                </div>
                <div class="form-row">
                    <label for="full_name">Nama Lengkap:</label>
                    <input v-model="formData.full_name" id="full_name" class="form-control" name="full_name" type="text">
                </div>
                <div class="form-row">
                    <label for="date_of_birth">Tanggal Lahir:</label>
                    <Datepicker :enable-time-picker="false" model-type="dd.MM.yyyy" v-model="formData.date_of_birth" id="date_of_birth" class="form-control" name="date_of_birth" type="text"></Datepicker>
                </div>
                <div class="form-row">
                    <label for="place_of_birth">Tempat Lahir:</label>
                    <textarea v-model="formData.place_of_birth" class="form-control" name="place_of_birth" type="text"></textarea>
                </div>
                <div class="form-row">
                    <label for="complete_address">Alamat Lengkap:</label>
                    <textarea v-model="formData.complete_address" id="complete_address" class="form-control" name="complete_address" type="text"></textarea>
                </div>
                <div class="form-row form-row-inline">
                    <label for="deceased">Almarhum:</label>
                    <input v-model="formData.deceased" class="form-check-input" id="deceased" name="deceased" type="checkbox">
                </div>
                <div class="form-row">
                    <label for="mother_id">Nama lengkap Ibu:</label>
                    <select v-model="formData.mother_id" class="form-select" id="mother_id" name="mother_id">
                        <option v-for="opt in motherChoices" :key="opt" :value="opt.value">{{ opt.title }}</option>
                    </select>
                </div>
                <div class="form-row">
                    <label for="father_id">Nama lengkap Ayah:</label>
                    <select v-model="formData.father_id" class="form-select" id="father_id" name="father_id">
                        <option v-for="opt in fatherChoices" :key="opt" :value="opt.value">{{ opt.title }}</option>
                    </select>
                </div>
                <div v-if="['grand', 'adult', 'child'].includes(formData.role)">
                    <div class="form-row">
                        <label for="spouse_full_name">Nama lengkap Suami/Istri:</label>
                        <input v-model="formData.spouse_full_name" id="spouse_full_name" class="form-control" name="spouse_full_name" type="text">
                    </div>
                    <div class="form-row">
                        <label for="spouse_date_of_birth">Tanggal Lahir Suami/Istri:</label>
                        <Datepicker :enable-time-picker="false" model-type="dd.MM.yyyy" v-model="formData.spouse_date_of_birth" id="spouse_date_of_birth" class="form-control" name="spouse_date_of_birth" type="text"></Datepicker>
                    </div>
                    <div class="form-row">
                        <label for="spouse_place_of_birth">Tempat Lahir Suami/Istri:</label>
                        <textarea v-model="formData.spouse_place_of_birth" id="spouse_place_of_birth" class="form-control" name="spouse_place_of_birth" type="text"></textarea>
                    </div>
                    <div class="form-row form-row-inline">
                        <label for="spouse_deceased">Almarhum Suami/Istri:</label>
                        <input v-model="formData.spouse_deceased" class="form-check-input" id="spouse_deceased" name="deceased" type="checkbox">
                    </div>
                    <div class="form-row">
                        <label for="mother_inlaws_full_name">Nama lengkap Mertua perempuan:</label>
                        <input v-model="formData.mother_inlaws_full_name" id="mother_inlaws_full_name" class="form-control" name="mother_inlaws_full_name" type="text">
                    </div>
                    <div class="form-row form-row-inline">
                        <label for="mother_inlaws_deceased">Almarhum Mertua perempuan:</label>
                        <input v-model="formData.mother_inlaws_deceased" class="form-check-input" id="mother_inlaws_deceased" name="mother_inlaws_deceased" type="checkbox">
                    </div>
                    <div class="form-row">
                        <label for="father_inlaws_full_name">Nama lengkap Mertua laki-laki:</label>
                        <input v-model="formData.father_inlaws_full_name" id="father_inlaws_full_name" class="form-control" name="father_inlaws_full_name" type="text">
                    </div>
                    <div class="form-row form-row-inline">
                        <label for="father_inlaws_deceased">Almarhum Mertua laki-laki:</label>
                        <input v-model="formData.father_inlaws_deceased" class="form-check-input" id="father_inlaws_deceased" name="father_inlaws_deceased" type="checkbox">
                    </div>
                    <div class="form-row">
                        <label for="father_inlaws_full_address">Alamat lengkap Mertua:</label>
                        <textarea v-model="formData.father_inlaws_full_address" id="father_inlaws_full_address" class="form-control" name="father_inlaws_full_address" type="text"></textarea>
                    </div>
                </div>
                <button class="btn btn-primary" type="submit">Submit</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'


export default {
    components: { Datepicker },
    data() {
        return {
            generations: [
                {
                    value: 'grand',
                    title: 'Gen 1'
                },
                {
                    value: 'adult',
                    title: 'Gen 2'
                },
                {
                    value: 'child',
                    title: 'Gen 3'
                },
                {
                    value: 'grandchild',
                    title: 'Gen 4'
                },
            ],
            motherChoices: [],
            fatherChoices: [],
            formData: {
                role: null,
                gender: null,
                full_name: null,
                date_of_birth: null,
                place_of_birth: null,
                complete_address: null,
                deceased: false,
                mother_id: null,
                father_id: null,
                spouse_full_name: null,
                spouse_date_of_birth: null,
                spouse_place_of_birth: null,
                spouse_deceased: false,
                father_inlaws_full_name: null,
                father_inlaws_full_address: null,
                father_inlaws_deceased: false,
                mother_inlaws_full_name: null,
                mother_inlaws_deceased: false,
            },
        }
    },
    methods: {
        postNewMember: function() {
            axios.post('/members', this.formData).then((response) => {
                window.location.reload();
            });
        },
        getParentsChoices: function(forRole) {
            axios.get(`/candidates?role=${forRole}`).then((response) => {
                this.motherChoices = response.data.female;
                this.fatherChoices = response.data.male;
            });
        },
    },
    watch: {
        'formData.role'(newRole) {
            this.getParentsChoices(newRole);
        },
    }
}
</script>

<style scoped>

</style>