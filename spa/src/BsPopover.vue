<script>
import { Popover } from 'bootstrap';

export default {
  name: 'BsPopover',

  template: `
    <slot/>
  `,
  props: {
    content: {
      required: false,
      default: '',
    },
    title: {
      default: 'My Popover',
    },
    trigger: {
      default: 'click',
    },
    delay: {
      default: 0,
    },
    html: {
      default: false,
    },
  },
  mounted() {
    // pass bootstrap popover options from props
    // to the bootstrap popover instance
    var options = this.$props
    const a = 5;
    //var ele = this.$slots.default[0].elm
    //new Popover(ele,options)
  }
};
</script>
