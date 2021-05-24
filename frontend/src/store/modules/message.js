const state = {
    content: null,
    type: null
  }
    
  const mutations = {
    updateMessage (state, message) {
      state.content = message.content;
      state.type = message.type;
      if (typeof message.timeout === 'undefined') {
        message.timeout = 3000
      }
      setTimeout(() => {state.content = null, state.type = null}, message.timeout)
    }
  }
  
  const actions = {
    message(context, message) {
      context.commit('updateMessage', message);
  
      if (typeof message.timeout === 'undefined') {
        message.timeout = 3000
      }
      setTimeout(() => {context.commit('updateMessage', null);}, message.timeout)
    },
  }
  
  
  export default {
    actions,
    state,
    mutations,
  }