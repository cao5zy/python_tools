#! /bin/python
import re
import fluentpy as _

'''
将下面的class都抓出来生成css名称，这样可以先集中精力在布局命名上
        <View className='coupon-footer'>
          <View className='coupon-footer-control'>
            <View className='coupon-footer-control-left'>
              <Image src={askImg} className='ask-sign' />
              <Text className='coupon-footer-control-left-text'>兑换说明</Text>
            </View>
            {/* coupon-footer-control-left */}
            <View className='coupon-footer-control-right'>
              <Text className='coupon-footer-control-right-text'>柜面核销</Text>
              <Image src={barImg} className='coupon-footer-control-right-bar' />
            </View>
            {/* coupon-footer-control-right */}
          </View>
          {/* coupon-footer-control */}
          <View className='coupon-footer-code'>
            <View className='coupon-footer-special' />
            <View className='coupon-footer-code-text' />
            <View className='coupon-footer-barcode' />
            <View className='coupon-footer-qrcode' />
            <View className='coupon-footer-comment' />
          </View>

'''
def get_class_name(lines):
    _(re.findall(r".*className='([\w\-]+)'.*", lines))\
    .filter(_.each != None) \
    .map(lambda n:'.'+n+' { }') \
    .map(print)


target_file = './generate_css.txt'

with open(target_file) as f:
    print(get_class_name(f.read()))

    
