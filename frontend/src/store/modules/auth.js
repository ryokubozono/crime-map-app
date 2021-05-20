export default {
    state: {
      userId: "",
      userToken: "",
      superUser: false
    },
    mutations: {
        updateUser(state, user) {
            state.userId = user.userId;
            state.userToken = user.userToken;
        },
        updateAdmin(state, admin) {
            state.superUser = admin.superUser;
        }
    },
    actions: {
        auth(context, user) {
            context.commit('updateUser', user);
        },
        admin(context, admin) {
            context.commit('updateAdmin', admin);
        }
    },
    modules: {},
    }