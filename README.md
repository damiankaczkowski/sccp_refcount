### sccp chan references count

# Install
```
git clone git@github.com:modulis/sccp_refcount.git
cd sccp_refcount
python setup.py install
```

# Cronjob example

```
*/15 * * * * root sccp_refcount -u{AMI_USER} -p{AMI_PASS} -H{AMI_HOST} -f {OUTPUT_FILE}
```
