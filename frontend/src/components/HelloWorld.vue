<template>
  <div>
    <h1>To-Do List</h1>
    <form @submit.prevent="addTodo">
      <input v-model="newTask" placeholder="Add a new task" required />
      <button type="submit">Add</button>
    </form>

    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input
          type="checkbox"
          v-model="todo.completed"
          @change="toggleComplete(todo)"
        />
        <span :class="{ completed: todo.completed }">{{ todo.task }}</span>
        <button @click="deleteTodo(todo.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTask: "",
      todos: [],
      apiUrl: "http://127.0.0.1:5000/api/todos", // Replace with your API URL
    };
  },
  mounted() {
    this.fetchTodos();
  },
  methods: {
    async fetchTodos() {
      try {
        const res = await fetch(this.apiUrl);
        if (!res.ok) throw new Error('Failed to fetch todos');
        this.todos = await res.json();
      } catch (error) {
        console.error(error);
      }
    },
    async addTodo() {
      try {
        const res = await fetch(this.apiUrl, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ task: this.newTask }),
        });
        if (!res.ok) throw new Error('Failed to add todo');
        const newTodo = await res.json();
        this.todos.push(newTodo);
        this.newTask = ""; // Reset input
      } catch (error) {
        console.error(error);
      }
    },
    async toggleComplete(todo) {
      try {
        await fetch(`${this.apiUrl}/${todo.id}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ completed: todo.completed }),
        });
      } catch (error) {
        console.error(error);
      }
    },
    async deleteTodo(id) {
      try {
        await fetch(`${this.apiUrl}/${id}`, { method: "DELETE" });
        this.todos = this.todos.filter((todo) => todo.id !== id);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style>
.completed {
  text-decoration: line-through;
}
</style>
