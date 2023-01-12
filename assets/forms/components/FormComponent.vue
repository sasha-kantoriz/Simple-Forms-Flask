<template>
    <div id="form" class="form-container">
        <div class="form-wrapper">
          <form @submit.prevent="formSubmit">
            <input name="name" class="form-control" type="text" placeholder="Your name" v-model="form.name"/>
            <input name="phone" class="form-control" type="text" placeholder="Phone number" v-model="form.phone"/>
            <input name="email" class="form-control" type="text" placeholder="Email address" v-model="form.email"/>
            <div class="child-input" v-for="(child, index) in children" :key="index">
                <input name="name" class="form-control form-control-sm" type="text" placeholder="Child name" v-model="child.name"/>
                <input name="phone" class="form-control form-control-sm" type="text" placeholder="Child phone" v-model="child.phone"/>
                <input name="email" class="form-control form-control-sm" type="text" placeholder="Child email" v-model="child.email"/>
            </div>

            <div class="form-buttons" role="group" aria-label="Basic outlined example">
              <button @click.prevent="addChild" class="btn btn-primary">Add child</button>
              <button type="submit" class="btn btn-primary">Submit</button>
              <button type="reset" @click="resetForm" class="btn btn-primary">Reset</button>
            </div>
          </form>
        </div>
    </div>

    <p v-for="(notification, index) in notifications" :key="notification">{{ notification }}</p>
</template>

<script>
import axios from 'axios';

export default {
  name: 'FormComponent',
  props: {
    msg: String
  },
  data() {
    return {
    notifications: [],
        children: [],
        form: {
            name: '',
            phone: '',
            email: '',
        },
    }
  },
  methods: {
    addChild() {
        this.children.push({
            name: '',
            phone: '',
            email: '',
        })
    },
    resetForm: function() {
        this.children = [];
        this.form = {};
    },
    async formSubmit(event) {
        let form = new FormData();
        form.append('name', this.form.name);
        form.append('phone', this.form.phone);
        form.append('email', this.form.email);
        let response = await axios.post('/submit', form);
        const parent_id = response.data.id;

        this.notifications.push(`Saved with ${response.data.id}`);

        this.children.forEach((child) => {
            let form = new FormData();
            form.append('child', true);
            form.append('parent_id', parent_id);
            form.append('name', child.name);
            form.append('phone', child.phone);
            form.append('email', child.email);
            axios.post('/submit', form).then(response => this.notifications.push(`Added child with ${response.data.id}`));
        });
        // reset form(s)
        this.form = {};
        this.children = [];
        // clear notifications
        setTimeout(this.clearNotifications, 5000);
    },
    clearNotifications: function() {
        this.notifications = [];
    }
  }
}
</script>

<style scoped>

</style>
