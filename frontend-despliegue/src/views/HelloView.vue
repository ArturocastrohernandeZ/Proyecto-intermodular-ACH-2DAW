<script setup>
import { ref } from 'vue'
import { getHello } from '@/services/helloService'
import HelloResult from '@/components/HelloResult.vue'

// Estado de la vista
const name = ref('')
const message = ref('')
const error = ref('')
const loading = ref(false)

// Acción: se ejecuta al enviar el formulario
async function saludar() {
  loading.value = true
  error.value = ''
  message.value = ''

  try {
    message.value = await getHello(name.value)
  } catch (e) {
    error.value = 'No se ha podido contactar con el backend. ¿Está arrancado?'
    console.error(e)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <section class="hello">
    <h1>Hello World</h1>

    <form class="hello__form" @submit.prevent="saludar">
      <label for="name">Tu nombre (opcional)</label>
      <input id="name" v-model="name" type="text" placeholder="Ana" />
      <button type="submit" :disabled="loading">
        {{ loading ? 'Cargando…' : 'Saludar' }}
      </button>
    </form>

    <HelloResult :message="message" :error="error" />
  </section>
</template>

<style scoped>
.hello__form {
  display: flex;
  flex-direction: column;
  gap: var(--space-s);
  max-width: 320px;
}

input {
  height: 52px;
  padding: 0 var(--space-m);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-m);
  background: var(--color-control-background);
  color: var(--color-on-surface);
  font: inherit;
}

input:focus {
  border: 2px solid var(--color-primary);
}

button {
  width: 230px;
  height: 52px;
  padding: 0 var(--space-l);
  border: none;
  border-radius: var(--radius-m);
  background: var(--color-primary);
  color: var(--color-on-primary);
  font: inherit;
  font-size: 15px;
  font-weight: 600;
  line-height: 22px;
  cursor: pointer;
}


button:hover:not(:disabled) {
  background: var(--color-primary-hover);
}

button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

button:disabled {
  background: var(--color-disabled);
  color: var(--color-on-disabled);
  cursor: wait;
}

@media (max-width: 600px) {
  button {
    width: 100%;
  }
}
</style>